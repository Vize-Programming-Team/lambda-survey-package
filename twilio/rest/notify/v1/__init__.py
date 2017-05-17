# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.base.version import Version
from twilio.rest.notify.v1.credential import CredentialList
from twilio.rest.notify.v1.service import ServiceList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Notify
        
        :returns: V1 version of Notify
        :rtype: V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._credentials = None
        self._services = None

    @property
    def credentials(self):
        """
        :rtype: CredentialList
        """
        if self._credentials is None:
            self._credentials = CredentialList(self)
        return self._credentials

    @property
    def services(self):
        """
        :rtype: ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1>'
