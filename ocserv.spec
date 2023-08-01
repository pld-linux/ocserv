# TODO: heimdal support
#
# Conditional build:
%bcond_with	kerberos5	# GSSAPI authentication (currently only MIT krb5 supported)
%bcond_without	oidc		# OpenID Connect authentication
%bcond_without	radius		# RADIUS support
#
Summary:	OpenConnect VPN server
Summary(pl.UTF-8):	Serwer VPN-a OpenConnect
Name:		ocserv
Version:	1.2.0
Release:	2
License:	GPL v2+
Group:		Applications/Networking
Source0:	ftp://ftp.infradead.org/pub/ocserv/%{name}-%{version}.tar.xz
# Source0-md5:	a73b32eac50aa3e46ae3b4a9f6140c59
Patch0:		%{name}-link.patch
URL:		http://ocserv.gitlab.io/www/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.11.3
%{?with_oidc:BuildRequires:	cjose-devel}
%{?with_oidc:BuildRequires:	curl-devel}
BuildRequires:	gnutls-devel >= 3.6.0
BuildRequires:	http-parser-devel
%{?with_oidc:BuildRequires:	jansson-devel}
# pkgconfig(krb5-gssapi)
%{?with_kerberos5:BuildRequires:	krb5-devel}
BuildRequires:	libev-devel >= 4
BuildRequires:	libmaxminddb-devel >= 1.0.0
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	libpcl-devel
BuildRequires:	libseccomp-devel
%{?with_kerberos5:BuildRequires:	libtasn1-devel >= 3.9}
BuildRequires:	libwrap-devel
BuildRequires:	lz4-devel >= 1:1.7
BuildRequires:	nettle-devel >= 2.7
BuildRequires:	oath-toolkit-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	protobuf-c-devel
%{?with_radius:BuildRequires:	radcli-devel >= 1.2.5}
BuildRequires:	readline-devel
BuildRequires:	systemd-devel
BuildRequires:	talloc-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gnutls >= 3.6.0
Requires:	libmaxminddb >= 1.0.0
Requires:	libnl >= 3.2
Requires:	nettle >= 2.7
%{?with_radius:Requires:	radcli >= 1.2.5}
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
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_oidc:--enable-oidc-auth} \
	%{!?with_kerberos5:--without-gssapi} \
	%{!?with_radius:--without-radius}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md TODO
%attr(755,root,root) %{_bindir}/occtl
%attr(755,root,root) %{_bindir}/ocpasswd
%attr(755,root,root) %{_bindir}/ocserv-fw
%attr(755,root,root) %{_sbindir}/ocserv
%attr(755,root,root) %{_sbindir}/ocserv-worker
%{_mandir}/man8/occtl.8*
%{_mandir}/man8/ocpasswd.8*
%{_mandir}/man8/ocserv.8*
