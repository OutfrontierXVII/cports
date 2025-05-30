pkgname = "perl-ipc-run"
pkgver = "20231003.0"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
depends = ["perl-io-tty"]
pkgdesc = "Perl system() and background procs w/ piping, redirs, ptys"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/dist/IPC-Run"
source = f"$(CPAN_SITE)/IPC/IPC-Run-{pkgver}.tar.gz"
sha256 = "eb25bbdf5913d291797ef1bfe998f15130b455d3ed02aacde6856f0b25e4fe57"
