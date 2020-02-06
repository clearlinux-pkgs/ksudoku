#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ksudoku
Version  : 19.12.2
Release  : 18
URL      : https://download.kde.org/stable/release-service/19.12.2/src/ksudoku-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/ksudoku-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/ksudoku-19.12.2.tar.xz.sig
Summary  : A logic-based symbol placement puzzle
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: ksudoku-bin = %{version}-%{release}
Requires: ksudoku-data = %{version}-%{release}
Requires: ksudoku-license = %{version}-%{release}
Requires: ksudoku-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : glu-dev
BuildRequires : libkdegames-dev
BuildRequires : mesa-dev
BuildRequires : qtbase-dev mesa-dev

%description
PROGRAM NAME  ksudoku
LICENSE       GPL v2
VERSION       0.3
AUTHOR        Francesco Rossi <redsh@email.it> 2005
DATE          29/9/2005

%package bin
Summary: bin components for the ksudoku package.
Group: Binaries
Requires: ksudoku-data = %{version}-%{release}
Requires: ksudoku-license = %{version}-%{release}

%description bin
bin components for the ksudoku package.


%package data
Summary: data components for the ksudoku package.
Group: Data

%description data
data components for the ksudoku package.


%package doc
Summary: doc components for the ksudoku package.
Group: Documentation

%description doc
doc components for the ksudoku package.


%package license
Summary: license components for the ksudoku package.
Group: Default

%description license
license components for the ksudoku package.


%package locales
Summary: locales components for the ksudoku package.
Group: Default

%description locales
locales components for the ksudoku package.


%prep
%setup -q -n ksudoku-19.12.2
cd %{_builddir}/ksudoku-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581031612
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581031612
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksudoku
cp %{_builddir}/ksudoku-19.12.2/COPYING %{buildroot}/usr/share/package-licenses/ksudoku/133efad5329acf364135c569ac01ec084c3d4647
cp %{_builddir}/ksudoku-19.12.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/ksudoku/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang ksudoku

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ksudoku

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.ksudoku.desktop
/usr/share/icons/hicolor/128x128/apps/ksudoku.png
/usr/share/icons/hicolor/16x16/apps/ksudoku.png
/usr/share/icons/hicolor/32x32/apps/ksudoku.png
/usr/share/ksudoku/4x4.desktop
/usr/share/ksudoku/4x4.xml
/usr/share/ksudoku/6x6.desktop
/usr/share/ksudoku/6x6.xml
/usr/share/ksudoku/Aztec.desktop
/usr/share/ksudoku/Aztec.xml
/usr/share/ksudoku/DoubleRoxdoku.desktop
/usr/share/ksudoku/DoubleRoxdoku.xml
/usr/share/ksudoku/Jigsaw.desktop
/usr/share/ksudoku/Jigsaw.xml
/usr/share/ksudoku/Killer_4x4.desktop
/usr/share/ksudoku/Killer_4x4.xml
/usr/share/ksudoku/Killer_9x9.desktop
/usr/share/ksudoku/Killer_9x9.xml
/usr/share/ksudoku/Mathdoku_4x4.desktop
/usr/share/ksudoku/Mathdoku_4x4.xml
/usr/share/ksudoku/Mathdoku_Settable.desktop
/usr/share/ksudoku/Mathdoku_Settable.xml
/usr/share/ksudoku/Nonomino.desktop
/usr/share/ksudoku/Nonomino.xml
/usr/share/ksudoku/Pentomino.desktop
/usr/share/ksudoku/Pentomino.xml
/usr/share/ksudoku/RoxdokuTwin.desktop
/usr/share/ksudoku/RoxdokuTwin.xml
/usr/share/ksudoku/Samurai.desktop
/usr/share/ksudoku/Samurai.xml
/usr/share/ksudoku/SamuraiRoxdoku.desktop
/usr/share/ksudoku/SamuraiRoxdoku.xml
/usr/share/ksudoku/Sohei.desktop
/usr/share/ksudoku/Sohei.xml
/usr/share/ksudoku/Tetromino.desktop
/usr/share/ksudoku/Tetromino.xml
/usr/share/ksudoku/TinySamurai.desktop
/usr/share/ksudoku/TinySamurai.xml
/usr/share/ksudoku/Windmill.desktop
/usr/share/ksudoku/Windmill.xml
/usr/share/ksudoku/XSudoku.desktop
/usr/share/ksudoku/XSudoku.xml
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-jigsaw.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-ksudoku_16x16.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-ksudoku_25x25.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-ksudoku_4x4.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-ksudoku_9x9.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-roxdoku_3x3x3.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-roxdoku_4x4x4.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-roxdoku_5x5x5.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-samurai.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-tiny_samurai.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku-xsudoku.png
/usr/share/ksudoku/icons/hicolor/128x128/actions/ksudoku.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-jigsaw.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-ksudoku_16x16.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-ksudoku_25x25.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-ksudoku_4x4.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-ksudoku_9x9.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-roxdoku_3x3x3.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-roxdoku_4x4x4.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-roxdoku_5x5x5.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-samurai.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-tiny_samurai.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku-xsudoku.png
/usr/share/ksudoku/icons/hicolor/16x16/actions/ksudoku.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-jigsaw.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-ksudoku_16x16.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-ksudoku_25x25.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-ksudoku_4x4.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-ksudoku_9x9.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-roxdoku_3x3x3.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-roxdoku_4x4x4.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-roxdoku_5x5x5.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-samurai.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-tiny_samurai.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku-xsudoku.png
/usr/share/ksudoku/icons/hicolor/22x22/actions/ksudoku.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-jigsaw.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-ksudoku_16x16.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-ksudoku_25x25.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-ksudoku_4x4.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-ksudoku_9x9.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-roxdoku_3x3x3.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-roxdoku_4x4x4.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-roxdoku_5x5x5.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-samurai.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-tiny_samurai.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku-xsudoku.png
/usr/share/ksudoku/icons/hicolor/32x32/actions/ksudoku.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-jigsaw.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-ksudoku_16x16.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-ksudoku_25x25.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-ksudoku_4x4.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-ksudoku_9x9.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-roxdoku_3x3x3.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-roxdoku_4x4x4.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-roxdoku_5x5x5.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-samurai.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-tiny_samurai.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku-xsudoku.png
/usr/share/ksudoku/icons/hicolor/48x48/actions/ksudoku.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-jigsaw.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-ksudoku_16x16.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-ksudoku_25x25.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-ksudoku_4x4.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-ksudoku_9x9.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-roxdoku_3x3x3.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-roxdoku_4x4x4.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-roxdoku_5x5x5.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-samurai.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-tiny_samurai.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku-xsudoku.png
/usr/share/ksudoku/icons/hicolor/64x64/actions/ksudoku.png
/usr/share/ksudoku/themes/abstraction.desktop
/usr/share/ksudoku/themes/abstraction.svg
/usr/share/ksudoku/themes/abstraction_preview.png
/usr/share/ksudoku/themes/default.desktop
/usr/share/ksudoku/themes/egyptian_preview.png
/usr/share/ksudoku/themes/ksudoku_egyptian.svg
/usr/share/ksudoku/themes/ksudoku_scrible.desktop
/usr/share/ksudoku/themes/ksudoku_scrible.svg
/usr/share/ksudoku/themes/scribble_preview.png
/usr/share/kxmlgui5/ksudoku/ksudokuui.rc
/usr/share/metainfo/org.kde.ksudoku.appdata.xml
/usr/share/xdg/ksudokurc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/ksudoku/index.cache.bz2
/usr/share/doc/HTML/de/ksudoku/index.docbook
/usr/share/doc/HTML/en/ksudoku/index.cache.bz2
/usr/share/doc/HTML/en/ksudoku/index.docbook
/usr/share/doc/HTML/es/ksudoku/index.cache.bz2
/usr/share/doc/HTML/es/ksudoku/index.docbook
/usr/share/doc/HTML/et/ksudoku/index.cache.bz2
/usr/share/doc/HTML/et/ksudoku/index.docbook
/usr/share/doc/HTML/fr/ksudoku/index.cache.bz2
/usr/share/doc/HTML/fr/ksudoku/index.docbook
/usr/share/doc/HTML/gl/ksudoku/index.cache.bz2
/usr/share/doc/HTML/gl/ksudoku/index.docbook
/usr/share/doc/HTML/it/ksudoku/index.cache.bz2
/usr/share/doc/HTML/it/ksudoku/index.docbook
/usr/share/doc/HTML/nl/ksudoku/index.cache.bz2
/usr/share/doc/HTML/nl/ksudoku/index.docbook
/usr/share/doc/HTML/pt/ksudoku/index.cache.bz2
/usr/share/doc/HTML/pt/ksudoku/index.docbook
/usr/share/doc/HTML/pt_BR/ksudoku/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ksudoku/index.docbook
/usr/share/doc/HTML/ru/ksudoku/index.cache.bz2
/usr/share/doc/HTML/ru/ksudoku/index.docbook
/usr/share/doc/HTML/sv/ksudoku/index.cache.bz2
/usr/share/doc/HTML/sv/ksudoku/index.docbook
/usr/share/doc/HTML/uk/ksudoku/index.cache.bz2
/usr/share/doc/HTML/uk/ksudoku/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksudoku/133efad5329acf364135c569ac01ec084c3d4647
/usr/share/package-licenses/ksudoku/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f ksudoku.lang
%defattr(-,root,root,-)

