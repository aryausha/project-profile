# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class WorkflowRealTimeStatisticsTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .workflows(sid="WWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .real_time_statistics().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RealTimeStatistics',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "longest_task_waiting_age": 100,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows/WWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RealTimeStatistics",
                "tasks_by_priority": {},
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "tasks_by_status": {
                    "reserved": 0,
                    "pending": 0,
                    "assigned": 0,
                    "wrapping": 0
                },
                "workflow_sid": "WWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "total_tasks": 100,
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .workflows(sid="WWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .real_time_statistics().fetch()

        self.assertIsNotNone(actual)
