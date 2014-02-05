# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       libsoup

# >> macros
# << macros

Summary:    Soup, an HTTP library implementation
Version:    2.44.2
Release:    1
Group:      System/Libraries
License:    LGPLv2
URL:        http://live.gnome.org/LibSoup
Source0:    http://download.gnome.org/sources/libsoup/2.44/%{name}-%{version}.tar.xz
Source100:  libsoup.yaml
Patch0:     disable-gtk-doc.patch
Requires:   glib-networking
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  glib-networking
BuildRequires:  gnome-common
BuildRequires:  intltool >= 0.25
BuildRequires:  python

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).


%package devel
Summary:    Header files for the Soup library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Libsoup is an HTTP library implementation in C. This package allows
you to develop applications that use the libsoup library.


%prep
%setup -q -n %{name}-%{version}/libsoup

# disable-gtk-doc.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
echo "EXTRA_DIST = missing-gtk-doc" > gtk-doc.make
USE_GNOME2_MACROS=1 NOCONFIGURE=1 gnome-autogen.sh
# << build pre

%configure --disable-static \
    --without-gnome \
    --disable-gtk-doc

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_datarootdir}/locale/*/LC_MESSAGES/*.mo
# >> files
%doc README COPYING NEWS AUTHORS
%{_libdir}/lib*.so.*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%dir %{_includedir}/libsoup-2.4
%{_includedir}/libsoup-2.4/libsoup
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#%doc %{_datadir}/gtk-doc/html/%{name}-2.4
# << files devel
