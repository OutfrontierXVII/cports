pkgname = "pinentry"
# Keep pkgver in sync with main/pinentry-qt
pkgver = "1.3.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-pinentry-tty",
    "--enable-pinentry-curses",
    "--enable-pinentry-gnome3",
    "--enable-pinentry-qt",
    "--enable-fallback-curses",
    "--enable-libsecret",
    "--enable-ncurses",
]
hostmakedepends = ["automake", "gettext", "libtool", "pkgconf"]
makedepends = [
    "gcr-devel",
    "gettext-devel",
    "gtk+3-devel",
    "libassuan-devel",
    "libgpg-error-devel",
    "libsecret-devel",
    "ncurses-devel",
    "qt6-qtbase-devel",
]
depends = ["virtual:pinentry-default!pinentry-curses-default"]
pkgdesc = "PIN or passphrase entry dialogs for GnuPG"
license = "GPL-2.0-or-later"
url = "https://www.gnupg.org/related_software/pinentry/index.html"
source = f"https://gnupg.org/ftp/gcrypt/pinentry/pinentry-{pkgver}.tar.bz2"
sha256 = "bc72ee27c7239007ab1896c3c2fae53b076e2c9bd2483dc2769a16902bce8c04"
options = ["empty"]


def post_install(self):
    # wipe the default symlink, user-chosen (curses is default)
    self.uninstall("usr/bin/pinentry")


def _frontend(name):
    @subpackage(f"pinentry-{name}")
    def _(self):
        self.subdesc = f"{name} frontend"

        if name == "qt":
            return [
                "usr/bin/pinentry-qt",
                "usr/share/applications/org.gnupg.pinentry-qt.desktop",
                "usr/share/pixmaps/pinentry.png",
            ]

        return [f"usr/bin/pinentry-{name}"]

    @subpackage(f"pinentry-{name}-default")
    def _(self):
        self.depends = [self.with_pkgver(f"pinentry-{name}")]
        self.provides = ["pinentry-default=0"]
        if name == "curses":
            self.install_if = [self.with_pkgver(f"pinentry-{name}")]
            # highest priority provider is curses
            self.provider_priority = 100

        return [f"@usr/bin/pinentry=>pinentry-{name}"]


for _fe in ["curses", "tty", "gnome3", "qt"]:
    _frontend(_fe)
