#
# spec file for package viabox
#
# cobbled together by thb@documentfoundation.org
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see http://www.gnu.org/licenses/ .
#


Name:           viabox
Version:        15.1.5
Release:        0
Summary:        Jukebox application to play your music and videos
License:        GPL-3.0+
Group:          Productivity/Multimedia/Sound/Players
Url:            https://github.com/r10s/viabox/archive/v15.1-beta.5.tar.gz
Source:         viabox-v15.1-beta.5.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  wxWidgets-wxcontainer-devel
BuildRequires:  xine-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Silverjuke is the easy-to-use jukebox with more than ten yeas of experience, see
http://viabox.net for further information.

%prep
%setup -q -n viabox-15.1-beta.5

%build
./autogen.sh --prefix=/usr --docdir=%{_docdir}/viabox
make %{?_smp_mflags}

%install
%makeinstall

%files
%defattr(-,root,root,-)
%docdir %{_docdir}
%dir %{_docdir}/viabox
%{_docdir}/viabox/CHANGES.md
%{_docdir}/viabox/LICENSE
%{_docdir}/viabox/README.md
%{_docdir}/viabox/command-line.md
%{_docdir}/viabox/dde.md
%{_docdir}/viabox/localization.md
%{_docdir}/viabox/plugins.md
%{_docdir}/viabox/scripting.md
%{_docdir}/viabox/skinning.md
%{_docdir}/viabox/user-guide.md
%{_docdir}/viabox/virtual-keyboards.md
%{_bindir}/viabox

%changelog
