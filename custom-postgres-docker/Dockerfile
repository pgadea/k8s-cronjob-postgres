FROM bitnami/postgresql:15.1.0-debian-11-r28

USER root

RUN mkdir /home/customscripts
RUN mkdir /home/backups

COPY backup.sh /home/customscripts
COPY restore.sh /home/customscripts

RUN chmod +x /home/customscripts/backup.sh
RUN chmod +x /home/customscripts/restore.sh

RUN chown -R 1001:1001 /home


ENV ALLOW_EMPTY_PASSWORD yes