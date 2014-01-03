Name:           kvm-qos
Version:        0.1
Release:        1%{?dist}
Summary:        A program that can help openstack partition the resource for virtual machines.

Group:          OpenStack
License:        GLPv2+
URL:            https://github.com/iamjackhu/kvm-qos/archive/master.zip
Patch0:         novaclient.patch
Patch1:         nova.patch

BuildRequires:  python
BuildRoot:      /tmp/%{name}-%{version}

%description

%prep

%build

%install

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc

%changelog
