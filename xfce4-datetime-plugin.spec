Summary:	A date and time plugin for the XFce4 panel
Summary(pl):	Plugin pokazuj±cy date i czas
Name:		xfce4-datetime-plugin
Version:	0.2
Release:	1
License:	GPL
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	ff4d9b545550fa72eba1c37a5d48edb6
Group:		X11/Applications
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	xfce4-panel-devel >= 4.0.0
Requires:	xfce4-panel >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An additional clock for the XFce4 panel which also shows the date,
with adjustable font.

%description -l pl
Plugin dla panelu XFce4 wy¶wietlaj±cy date i czas, wyposa¿ony w kalendarz.

%prep
%setup -q

%build
%{configure}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
