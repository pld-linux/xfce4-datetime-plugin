Summary:	A date and time plugin for the XFce4 panel
Summary(pl):	Wtyczka panelu XFce4 pokazuj�ca dat� i czas
Name:		xfce4-datetime-plugin
Version:	0.3.0
Release:	1
License:	GPL
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	fec04ccaf62534143ec65935b93b8d19
Group:		X11/Applications
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	xfce4-panel-devel >= 4.0.0
Requires:	xfce4-panel >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An additional clock for the XFce4 panel which also shows the date,
with adjustable font.

%description -l pl
Wtyczka dla panelu XFce4 wy�wietlaj�ca dat� i czas, wyposa�ona w
kalendarz.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang xfce4-datetime

%clean
rm -rf $RPM_BUILD_ROOT

%files -f xfce4-datetime.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
