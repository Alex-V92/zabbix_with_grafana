#
# $Git: Makefile.am 0.0-2-1 2022-06-15 12:34:22+03:00 dsyakupo $
#
AUTOMAKE_OPTIONS = -Wno-portability
#
PACKAGE          = zabbix-api
PRODHOST         = 0400itmon02
HOSTNAME         = $(shell hostname)
FAMILY           = $(shell grep -qPi '(ubuntu|debian)' /etc/os-release 2>/dev/null && echo "debian" || echo "redhat")
PACKAGEVERSION   = $(shell test -f ../VERSION && head -n 1 ../VERSION | cut -f1 -d' ')
ETC              = /etc
logconfdir       = ${ETC}/logrotate.d
logconf_DATA     = .${logconfdir}/${PACKAGE}
logdir           = /var/log/${PACKAGE}
cronddir         = ${ETC}/cron.d
crond_DATA       = .${cronddir}/${PACKAGE}
datadir          = /data/app/${PACKAGE}
data_DATA        = $(wildcard *.py)
DESTDIR          =

$(logconf_DATA): ${PACKAGE}.logrotated
	$(shell) mkdir -p .${logconfdir}
	$(shell) cp -fv $< $@

$(crond_DATA): ${PACKAGE}.crond
	$(shell) mkdir -p .${cronddir}
	$(shell) cp -fv $< $@

install-data-hook:
	$(shell) test "${HOSTNAME}" != "${PRODHOST}" && rm -fv ${cronddir}/${PACKAGE} || true
	$(shell) chmod +x ${datadir}/*.py || true
	$(shell) mkdir -p ${logdir}

uninstall-hook:
	$(shell) echo "don't forget to decide on the data in the log directory - ${logdir}"

clean-local:
	-rm -rf .${ETC}
