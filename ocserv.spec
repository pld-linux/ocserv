Summary:	OpenConnect VPN server
Summary(pl.UTF-8):	Serwer VPN-a OpenConnect
Name:		ocserv
Version:	0.8.7
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	ftp://ftp.infradead.org/pub/ocserv/%{name}-%{version}.tar.xz
# Source0-md5:	79c00132c3366bb60546f256068211eb
URL:		http://www.infradead.org/ocserv/
BuildRequires:	autogen
BuildRequires:	autogen-devel
BuildRequires:	dbus-devel >= 1.1.1
BuildRequires:	gnutls-devel >= 3.1.10
BuildRequires:	http-parser-devel
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	libpcl-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libwrap-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	protobuf-c-devel
BuildRequires:	readline-devel
BuildRequires:	systemd-devel
BuildRequires:	talloc-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	dbus-libs >= 1.1.1
Requires:	gnutls >= 3.1.10
Requires:	libnl >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenConnect server (ocserv) is an SSL VPN server. Its purpose is to be
a secure, small, fast and configurable VPN server. It implements the
OpenConnect SSL VPN protocol, and has also (currently experimental)
compatibility with clients using the AnyConnect SSL VPN protocol. The
OpenConnect VPN protocol uses the standard IETF security protocols
such as TLS 1.2, and Datagram TLS to provide the secure VPN service.
The server is implemented primarily for the GNU/Linux platform but its
code is designed to be portable to other UNIX variants as well.

%description -l pl.UTF-8
Serwer OpenConnect (ocserv) to serwer VPN-u SSL. Celem projektu jest
bezpieczny, mały, szybki i konfigurowalny serwer VPN. Implementuje
protokół VPN-u SSL OpenConnect, zapewnia także (obecnie
eksperymentalną) zgodność z klientami wykorzystującymi protokół VPN
SSL AnyConnect. Protokół VPN OpenConnect wykorzystuje standardowe
protokoły bezpieczeństwa IETF, takie jak TLS 1.2 oraz Datagram TLS w
celu zapewnienia bezpieczeństwa usługi VPN. Serwer jest
zaimplementowany głównie dla platformy GNU/Linux, ale kod jest
zaprojektowany jako zgodny także z innymi wariantami uniksów.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README TODO
%attr(755,root,root) %{_bindir}/occtl
%attr(755,root,root) %{_bindir}/ocpasswd
%attr(755,root,root) %{_sbindir}/ocserv
%{_mandir}/man8/occtl.8*
%{_mandir}/man8/ocpasswd.8*
%{_mandir}/man8/ocserv.8*
