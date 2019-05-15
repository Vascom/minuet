Name:           minuet
Version:        19.04.1
Release:        2%{?dist}
Summary:        A KDE Software for Music Education
#OFL license for bundled Bravura.otf font
#and BSD license for cmake/FindFluidSynth.cmake
License:        GPLv2+ and OFL
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules >= 5.15.0
BuildRequires:  kf5-filesystem
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core) >= 5.7.0
BuildRequires:  cmake(Qt5Gui) >= 5.7.0
BuildRequires:  cmake(Qt5Qml) >= 5.7.0
BuildRequires:  cmake(Qt5Quick) >= 5.7.0
BuildRequires:  cmake(Qt5QuickControls2) >= 5.7.0
BuildRequires:  cmake(Qt5Svg) >= 5.7.0
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  libappstream-glib
# Runtime requirement
Requires:       qt5-qtquickcontrols2
Requires:       hicolor-icon-theme
Requires:       %{name}-data

Provides:       bundled(font(bravura))

%description
Application for Music Education.

Minuet aims at supporting students and teachers in many aspects
of music education, such as ear training, first-sight reading,
solfa, scales, rhythm, harmony, and improvisation.
Minuet makes extensive use of MIDI capabilities to provide a
full-fledged set of features regarding volume, tempo, and pitch
changes, which makes Minuet a valuable tool for both novice and
experienced musicians.

%package devel
Summary:        Minuet: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for Minuet.

%package data
Summary:        Minuet: Data files
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildArch:      noarch

%description data
Data files for Minuet.

%prep
%autosetup
chmod -x src/app/org.kde.%{name}.desktop

%build
mkdir build
pushd build
    %cmake_kf5 ..
    %make_build
popd

%install
pushd build
  %make_install
popd
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%doc README*
%license COPYING*
%{_datadir}/applications/org.kde.%name.desktop
%{_kf5_metainfodir}/org.kde.%name.appdata.xml
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/%{name}
%{_kf5_libdir}/libminuetinterfaces.so.*
%{_qt5_plugindir}/%{name}

%files devel
%doc README*
%license COPYING*
%{_includedir}/%{name}
%{_kf5_libdir}/libminuetinterfaces.so

%files data
%{_kf5_datadir}/%{name}


%changelog
* Wed May 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.04.1-2
- Added gcc-c++ to BR
- Data in separate subpackage
- Correct licensing

* Mon May 13 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.04.1-1
- First release for fedora
