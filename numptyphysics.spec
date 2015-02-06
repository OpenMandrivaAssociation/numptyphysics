Summary:	A crayon-drawing based physics puzzle game 
Name:		numptyphysics
Version:	0.3.3
Release:	3
License:	GPLv3+
Group:		Games/Puzzles
Url:		http://numptyphysics.garage.maemo.org/
# git clone git://github.com/harmattan/numptyphysics.git
# cd numptyphysics
# git archive --format=tar --prefix=numptyphysics-0.3.3/ 0.3.3 | \
# gzip > ../numptyphysics-0.3.3.tar.gz
Source0:	%{name}-%{version}.tar.gz
Source1:	numptyphysics.desktop
Source10:	numptyphysics-levels.tar.gz
Patch2:		numptyphysics-0.3.3.fixclose.patch
Patch3:		numptyphysics-0.3.3.fixmake.patch
BuildRequires:	desktop-file-utils
BuildRequires:	vim-common
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(x11)

%description
Harness gravity with your crayon and set about creating blocks, ramps,
levers, pulleys and whatever else you fancy to get the little red thing to
the little yellow thing.

%files
%{_bindir}/numptyphysics
%{_datadir}/numptyphysics
%{_datadir}/pixmaps/numptyphysics.png
%{_datadir}/applications/numptyphysics.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch2 -p 1 -b .fixclose
%patch3 -p 1 -b .fixmake

%build
export LIBS="-lz -lX11"
%make

%install
%makeinstall_std

# Directory structure
install -d %{buildroot}%{_datadir}/numptyphysics
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/pixmaps

# Files
install -pm 644 data/numptyphysics.png %{buildroot}%{_datadir}/pixmaps/numptyphysics.png

# Additional levels
tar xzf %{SOURCE10} -C %{buildroot}%{_datadir}/numptyphysics
mv -f %{buildroot}%{_datadir}/numptyphysics/numptyphysics-levels/*.nph %{buildroot}%{_datadir}/numptyphysics/
rm -rf %{buildroot}%{_datadir}/numptyphysics/numptyphysics-levels

# Icon
desktop-file-install %{SOURCE1} \
	--dir=%{buildroot}%{_datadir}/applications

