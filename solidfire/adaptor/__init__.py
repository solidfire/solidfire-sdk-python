#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.
"""Module implements the generated adaptor calls from solidfire.Element"""
from solidfire.adaptor.schedule_adaptor import ScheduleAdaptor
from solidfire.models import GetNodeStatsResult

class ElementServiceAdaptor(object):
    """
    This class contains the implementation of the generated adaptor calls from
    solidfire.Element.
    """
    @staticmethod
    def get_node_stats(element, params, since, deprecated):
        """
        This adaptor includes the original Node ID from the request in the
        response object. It is returned as null from the original API call.

        :param element: an instance of Element
        :type element: Element

        :param params: the parameters supplied to the get_node_stats call
        :type params: dict

        :param since: service method inception version
        :type since: float or str or None

        :param deprecated: service method deprecation version
        :type deprecated: float or str or None

        :returns: a response
        :rtype: GetNodeStatsResult
        """

        result = element.send_request(
            'GetNodeStats',
            GetNodeStatsResult,
            params,
            since,
            deprecated
        )

        result.node_stats.node_id = params["nodeID"]

        return result

    @staticmethod
    def invoke_sfapi(element, params, since, deprecated):
        if "parameters" in params:
            return element.send_request(
                params["method"],
                dict,
                params["parameters"],
                since,
                deprecated
            )
        else:
            return element.send_request(
                params["method"],
                dict,
                since=since,
                deprecated=deprecated
            )

    @staticmethod
    def get_schedule(element, params, since, deprecated):
        """
        Calls to this static method should ONLY originate from the
        get_schedule method in the Element class. DO NOT CALL THIS directly.
        Documentation here is intentionally brief.
        """

        return ScheduleAdaptor.get_schedule(element, params,
                                            since, deprecated)

    @staticmethod
    def list_schedules(element, params, since, deprecated):
        """
        Calls to this static method should ONLY originate from the
        list_schedules method in the Element class. DO NOT CALL THIS directly.
        Documentation here is intentionally brief.
        """

        return ScheduleAdaptor.list_schedules(element, params,
                                              since, deprecated)

    @staticmethod
    def modify_schedule(element, params, since, deprecated):
        """
        Calls to this static method should ONLY originate from the
        modify_schedules method in the Element class. DO NOT CALL THIS
        directly. Documentation here is intentionally brief.
        """

        return ScheduleAdaptor.modify_schedule(element, params,
                                               since, deprecated)

    @staticmethod
    def create_schedule(element, params, since, deprecated):
        """
        Calls to this static method should ONLY originate from the
        create_schedules method in the Element class. DO NOT CALL THIS
        directly. Documentation here is intentionally brief.
        """

        return ScheduleAdaptor.create_schedule(element, params,
                                               since, deprecated)
