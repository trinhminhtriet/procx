Name: procx
Version: 0.1.0
Release: 1%{?dist}
License: MIT
Summary: ProcX is an interactive command-line tool for quickly searching and terminating processes, offering a streamlined alternative to traditional kill.
Url: https://github.com/trinhminhtriet/%{name}
Source0: %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires: cargo
BuildRequires: rust
BuildRequires: gcc
	
%description
ProcX is an interactive command-line tool for quickly searching and terminating processes, offering a streamlined alternative to traditional kill.
	
%prep
%autosetup -p1
	
%build
cargo build --release

%install
install -Dpm 755 target/release/procx %{buildroot}%{_bindir}/procx

rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json

%files
%license LICENSE
%doc README.md
%{_bindir}/procx
	
%changelog
* Thu Oct 24 2024 Triet Trinh <contact@trinhminhtriet.com> 0.1.0
- new package

%autochangelog
