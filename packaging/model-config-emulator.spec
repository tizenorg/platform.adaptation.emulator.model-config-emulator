%define debug_package %{nil}

Name:		model-config-emulator
Summary:	A Model configuration
Version:	0.0.2
Release:	0
Group:		System/Configuration
License:	Apache-2.0
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz

%description
Model configuration data package

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/config

%define config_xml model-config_mobile.xml

%if "%{?profile}" == "wearable"
%define config_xml model-config_wearable.xml
%endif

%if "%{?profile}" == "tv"
%define config_xml model-config_tv.xml
%endif

%if "%{?profile}" == "mobile"
%define config_xml model-config_mobile.xml
%endif

cp -f %{config_xml} %{buildroot}%{_sysconfdir}/config/model-config.xml

%files
%config %{_sysconfdir}/config/model-config.xml
%manifest model-config.manifest
%license LICENSE.Apache-2.0
