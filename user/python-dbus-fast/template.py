pkgname = "python-dbus-fast"
pkgver = "2.44.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # these fail since pytest-asyncio 1.0.0
    "--deselect",
    "tests/test_aio_low_level.py::test_sending_signals_between_buses",
    "--deselect",
    "tests/test_disconnect.py::test_bus_disconnect_before_reply",
    "--deselect",
    "tests/test_disconnect.py::test_unexpected_disconnect",
    "--deselect",
    "tests/test_fd_passing.py::test_high_level_service_fd_passing",
    "--deselect",
    "tests/test_fd_passing.py::test_sending_file_descriptor_with_proxy",
    "--deselect",
    "tests/test_tcp_address.py::test_tcp_connection_with_forwarding",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-poetry-core",
    "python-setuptools",
]
makedepends = [
    "python-devel",
]
depends = ["python"]
checkdepends = [
    "dbus",
    "python-gobject",
    "python-pytest-asyncio",
    "python-pytest-timeout",
]
pkgdesc = "DBus library for python"
license = "MIT"
url = "https://pypi.org/project/dbus-fast"
source = f"https://github.com/Bluetooth-Devices/dbus-fast/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1f25e21eb7c6f771b53e45caba9ea7ecd640b3d39fb1cb68b3cdc8bc8f9bc002"


def post_prepare(self):
    # Requires pytest_codspeed
    self.rm("tests/benchmarks", recursive=True)


def post_install(self):
    self.install_license("LICENSE")
