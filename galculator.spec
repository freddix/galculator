Summary:	A GTK+ based scientific calculator
Name:		galculator
Version:	2.1.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/galculator/%{name}-%{version}.tar.bz2
# Source0-md5:	01c97ec3e18c26c64af78dca9f700d43
Patch0:		%{name}-desktop.patch
URL:		http://galculator.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ based scientific calculator with ordinary notation/reverse
polish notation, different number bases (DEC, HEX, OCT, BIN) and
different angle bases (DEG, RAD, GRAD).

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{da_DK,kk_KZ}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/galculator.png
%{_iconsdir}/hicolor/*/apps/galculator.svg
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

