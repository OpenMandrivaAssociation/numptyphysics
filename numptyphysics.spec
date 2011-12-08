Name:           numptyphysics
Version:        0.3
Release:        0.6.20080925svn
Summary:        A crayon-drawing based physics puzzle game 

Group:          Games/Puzzles
License:        GPLv3+
URL:            http://numptyphysics.garage.maemo.org/
# svn co -r81 https://garage.maemo.org/svn/numptyphysics/trunk numptyphysics
# tar czf numptyphysics.tar.gz numptyphysics --exclude .svn
Source0:        numptyphysics.tar.gz
Source1:        numptyphysics.desktop
Source10:       numptyphysics-levels.tar.gz
Patch0:         numptyphysics-0.3-gcc43.patch
Patch1:         numptyphysics-0.3-doublefree.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  SDL_image-devel
BuildRequires:  desktop-file-utils

%description
Harness gravity with your crayon and set about creating blocks, ramps,
levers, pulleys and whatever else you fancy to get the little red thing to
the little yellow thing.


%prep
%setup -q -n %{name}
%patch0 -p1 -b .gcc43
%patch1 -p1 -b .doublefree

%build
# Note the ARCH variable doesn't denote real arch. It's just used to hit a
# conditional that we're not compiling with mingw
make %{?_smp_mflags}    \
        ARCH=i686       \
        CCOPTS="%{optflags} -IBox2D/Include"


%install
rm -rf ${buildroot}

# Directory structure
install -d %{buildroot}%{_datadir}/numptyphysics
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/pixmaps

# Files
install -pm 644 *.png *.nph *.jpg %{buildroot}%{_datadir}/numptyphysics
install -pm 755 i686/Game %{buildroot}%{_bindir}/numptyphysics
install -pm 644 debian/numptyphysics64.png %{buildroot}%{_datadir}/pixmaps/numptyphysics.png

# Additional levels
tar xzf %{SOURCE10} -C %{buildroot}%{_datadir}/numptyphysics
mv -f %{buildroot}%{_datadir}/numptyphysics/numptyphysics-levels/*.nph %{buildroot}%{_datadir}/numptyphysics/
rm -rf %{buildroot}%{_datadir}/numptyphysics/numptyphysics-levels

# Icon
desktop-file-install %{SOURCE1} \
        --dir=%{buildroot}%{_datadir}/applications


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/numptyphysics
%{_datadir}/numptyphysics
%{_datadir}/pixmaps/numptyphysics.png
%{_datadir}/applications/numptyphysics.desktop

