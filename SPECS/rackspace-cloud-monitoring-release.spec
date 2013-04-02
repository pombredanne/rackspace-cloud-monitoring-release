
Name:           rackspace-cloud-monitoring-release 
Version:        1.0
Release:        1.{?dist}

Summary:        Rackspace Cloud Monitoring repository configuration

Group:          System Environment/Base 
License:        Rackspace Cloud Monitoring End User Agreement 
URL:            http://cloudmonitoring.rackspace.com

Source0:        RACKSPACE-CLOUD-MONITORING-GPG-KEY 

Source1:        rackspace-cloud-monitoring.repo.el5	
Source2:        rackspace-cloud-monitoring.repo.el6	
Source3:        rackspace-cloud-monitoring.repo.centos5	
Source4:        rackspace-cloud-monitoring.repo.centos6	
Source5:        rackspace-cloud-monitoring.repo.fedora16
Source6:        rackspace-cloud-monitoring.repo.fedora17

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Provides:       rackspace-cloud-monitoring

%description
This package contains the Rackspace Cloud Monitoring repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RACKSPACE-CLOUD-MONITORING-GPG-KEY

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%if 0%{?el5}
if [ %{?dist} == .centos5 ] # hacky...
then
install -pm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
else
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
fi
%endif

%if 0%{?el6}
%if 0%{?centos} == 6
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
%else
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
%endif
%endif

%if 0%{?fedora} == 16
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
%endir

%if 0%{?fedora} == 17
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
%endir


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog
* Tue Apr 02 2013 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0-1
- New package for Rackspace Monitoring Release