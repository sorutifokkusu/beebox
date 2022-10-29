echo "Install script starting"
sleep 5
geom disk list
sleep 5
read -r "device?Please write device name:"
DCP3=($device"p3")
DCP2=($device"p2")
DCP1=($device"p1")

gpart create -s gpt $device
gpart add -t efi -l efi -s 256M $device
newfs_msdos /dev/$DCP1
gpart add -t freebsd-swap -s 4G $device
gpart add -t freebsd-zfs -l ravynOS $device
zpool create -f -R /mnt -O mountpoint=/ -O atime=off -O canmount=off -O compression=on ravynOS $DCP3
sleep 2
zfs create -o canmount=off -o mountpoint=none ravynOS/ROOT
zfs create -o mountpoint=/ ravynOS/ROOT/default
zpool set bootfs=ravynOS/ROOT/default ravynOS
mkdir /tmp/efi
sleep 2
mount -t msdosfs /dev/devicep1 /tmp/efi
mkdir -p /tmp/efi/efi/boot
cp /boot/loader.efi /tmp/efi/efi/boot/bootx64.efi
cp /boot/loader.efi /tmp/efi/efi/boot/loader.efi
umount /tmp/efi
sleep 5
echo "before cat"
cat >> /tmp/excludes

echo "after cat"
sleep 10
cd /sysroot
sleep 2
echo "cpdup, drink a cup of coffee"
cpdup -uIof -X /tmp/excludes . /mnt
echo "done"
chroot /mnt /usr/bin/zsh
/usr/sbin/bsdinstall config
/usr/sbin/bsdinstall entropy
/usr/sbin/pw userdel -n liveuser
/usr/sbin/pw groupdel -n liveuser
rm -rf /Users/liveuser
rm -rf /var/db/pkg
mv /etc/rc.conf.local /etc/rc.conf
echo "editing rc.conf"
ee /etc/rc.conf

echo "editing loader.conf"
ee boot/loader.conf
