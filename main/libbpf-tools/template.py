pkgname = "libbpf-tools"
pkgver = "0.35.0"
pkgrel = 0
archs = ["aarch64", "ppc64le", "riscv64", "x86_64"]
build_wrksrc = "libbpf-tools"
build_style = "makefile"
make_build_args = [
    "prefix=/usr",
    "V=1",
    "APP_PREFIX=bpf-",
    "BPFTOOL=bpftool",
    "BPFTOOL_OUTPUT=/usr/bin/bpftool",
    "USE_BLAZESYM=0",
]
make_install_args = [*make_build_args]
hostmakedepends = [
    "bpftool",
    "pkgconf",
]
makedepends = [
    "argp-standalone",
    "libbpf-devel",
    "linux-headers",
]
pkgdesc = "Standalone eBPF programs from BCC"
license = "LGPL-2.1-only OR BSD-2-Clause"
url = "https://github.com/iovisor/bcc/tree/master/libbpf-tools"
source = f"https://github.com/iovisor/bcc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7adf1716d2a3df6802c3bb17664d79b9d68d7316a6773eb08d6e691c5ff0b2fc"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
    "LDFLAGS": ["-largp"],
}
# check: no tests
# distlicense: no actual bsd license in the folders, just headers
options = ["!check", "!distlicense"]
