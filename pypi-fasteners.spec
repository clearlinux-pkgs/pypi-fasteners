#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-fasteners
Version  : 0.17.3
Release  : 65
URL      : https://files.pythonhosted.org/packages/bd/f4/148f44998c1bdb064a508e7cbcf9e50b34572b3d36fcc378a5d61b7dc8c5/fasteners-0.17.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/bd/f4/148f44998c1bdb064a508e7cbcf9e50b34572b3d36fcc378a5d61b7dc8c5/fasteners-0.17.3.tar.gz
Summary  : A python package that provides useful locks
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-fasteners-license = %{version}-%{release}
Requires: pypi-fasteners-python = %{version}-%{release}
Requires: pypi-fasteners-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
Fasteners
=========
[![Documentation status](https://readthedocs.org/projects/fasteners/badge/?version=latest)](https://readthedocs.org/projects/fasteners/?badge=latest)
[![Downloads](https://img.shields.io/pypi/dm/fasteners.svg)](https://pypi.python.org/pypi/fasteners/)
[![Latest version](https://img.shields.io/pypi/v/fasteners.svg)](https://pypi.python.org/pypi/fasteners/)

%package license
Summary: license components for the pypi-fasteners package.
Group: Default

%description license
license components for the pypi-fasteners package.


%package python
Summary: python components for the pypi-fasteners package.
Group: Default
Requires: pypi-fasteners-python3 = %{version}-%{release}

%description python
python components for the pypi-fasteners package.


%package python3
Summary: python3 components for the pypi-fasteners package.
Group: Default
Requires: python3-core
Provides: pypi(fasteners)

%description python3
python3 components for the pypi-fasteners package.


%prep
%setup -q -n fasteners-0.17.3
cd %{_builddir}/fasteners-0.17.3
pushd ..
cp -a fasteners-0.17.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656405572
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-fasteners
cp %{_builddir}/fasteners-0.17.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-fasteners/987f2e77cc1fa9c15dc5b849c5fbd7534407bb2a
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-fasteners/987f2e77cc1fa9c15dc5b849c5fbd7534407bb2a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
