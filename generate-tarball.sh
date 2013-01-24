#! /bin/sh

rm -fr resources
git clone --depth 1 git://github.com/psi-plus/resources.git
rev=$(cd resources && git log -1 --pretty=%h skins)
pkgrev=$(date +%Y%m%d)git${rev}
psiver=0.16-${pkgrev}
tar -C resources/ -czf psi-plus-skins-${psiver}.tar.gz skins

