Summary:	Beeps the PC speaker controlling frequency, duration, repetitions, etc.
Summary(pl):	Piszczy na g³o¶niczku PC kontroluj±c czêstotliwo¶æ, d³ugo¶æ, powtórzenia itp.
Name:		beep
Version:	1.2.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.johnath.com/beep/%{name}-%{version}.tar.gz
# Source0-md5:	d541419fd7e5642952d7b48cbb40c712
URL:		http://johnath.com/beep/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
beep does what you'd expect: it beeps. But unlike printf("\a"), beep
allows you to control pitch, duration, and repetitions. Its job is to
live inside shell/perl scripts and allow more granularity than one has
otherwise. It is controlled completely through command line options.
It's not supposed to be complex, and it isn't - but it makes system
monitoring (or whatever else it gets hacked onto) that much more
informative.

%description -l pl
beep robi to, czego mo¿na siê spodziewaæ: piszczy. Ale w
przeciwieñstwie do printf("\a"), pozwala kontrolowaæ wysoko¶æ d¼wiêku,
czas trwania i powtórzenia. Jego zadaniem jest ¿yæ w skryptach Perla
lub pow³oki i pozwalaæ na wiêcej, ni¿ mo¿na zrobiæ bez niego.
Programem w ca³o¶ci steruje siê z linii poleceñ. Nie ma on byæ
skomplikowany - ale pozwala na bardziej informacyjne monitorowanie
systemu (czy cokolwiek, do czego zostanie u¿yty).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install beep $RPM_BUILD_ROOT%{_bindir}
gzip -dc beep.1.gz > $RPM_BUILD_ROOT%{_mandir}/man1/beep.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
