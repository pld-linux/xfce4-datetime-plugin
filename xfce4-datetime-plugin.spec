Summary:	A date and time plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka panelu Xfce pokazująca datę i czas
Name:		xfce4-datetime-plugin
Version:	0.6.2
Release:	3
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-datetime-plugin/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	fe604a251eadbc5b0f2b4737b85d92c8
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-datetime-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	gtk+2-devel >= 2:2.24.0
BuildRequires:	intltool
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxfce4ui-devel >= 4.8.0
BuildRequires:	libxfce4util-devel >= 4.8.0
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
Requires:	gtk+2 >= 2:2.24.0
Requires:	libxfce4ui >= 4.8.0
Requires:	libxfce4util >= 4.8.0
Requires:	xfce4-panel >= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An additional clock for the Xfce panel which also shows the date, with
adjustable font.

%description -l pl.UTF-8
Wtyczka dla panelu Xfce wyświetlająca datę i czas, wyposażona w
kalendarz.

%prep
%setup -q

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
# just a copy of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libdatetime.so
%{_datadir}/xfce4/panel/plugins/datetime.desktop
