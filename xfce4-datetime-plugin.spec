Summary:	A date and time plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka panelu Xfce pokazująca datę i czas
Name:		xfce4-datetime-plugin
Version:	0.6.1
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-datetime-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	e82f51ff0e75a63e5cbd139e43e094f9
Patch0:		%{name}-ui.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-datetime-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An additional clock for the Xfce panel which also shows the date, with
adjustable font.

%description -l pl.UTF-8
Wtyczka dla panelu Xfce wyświetlająca datę i czas, wyposażona w
kalendarz.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libdatetime.so
%{_datadir}/xfce4/panel-plugins/datetime.desktop
