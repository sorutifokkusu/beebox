echo "Install script starting"
sleep 5s


gpart create -s gpt vtbd0
gpart add -t efi -l efi -s 256M vtbd0
newfs_msdos /dev/vtbd0p1
gpart add -t freebsd-swap -s 4G vtbd0
gpart add -t freebsd-zfs -l ravynOS vtbd0
zpool create -f -R /mnt -O mountpoint=/ -O atime=off -O canmount=off -O compression=on ravynOS vtbd0p3
sleep 2s
zfs create -o canmount=off -o mountpoint=none ravynOS/ROOT
zfs create -o mountpoint=/ ravynOS/ROOT/default
zpool set bootfs=ravynOS/ROOT/default ravynOS
mkdir /tmp/efi
sleep 2s
mount -t msdosfs /dev/devicep1 /tmp/efi
mkdir -p /tmp/efi/efi/boot
cp /boot/loader.efi /tmp/efi/efi/boot/bootx64.efi
cp /boot/loader.efi /tmp/efi/efi/boot/loader.efi
umount /tmp/efi
sleep 5s
echo "before cat"
cat >> /tmp/excludes

echo "after cat"
sleep 2s
cd /sysroot
sleep 2s
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
