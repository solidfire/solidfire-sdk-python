#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.

from solidfire.results import GetNodeStatsResult


class ElementServiceAdaptor:
    @staticmethod
    def get_node_stats(params, result):
        """
        This adaptor includes the original Node ID from the request in the
        response object. It is returned as null from the original API call.

        :param params:
        :type params: dict

        :param result:
        :type result: GetNodeStatsResult

        :returns: a response
        :rtype: GetNodeStatsResult
        """

        result.node_stats.node_id = params["nodeID"]

        return result
