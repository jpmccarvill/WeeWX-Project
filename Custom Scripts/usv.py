import weewx.units

weewx.units.obs_group_dict['usv'] = 'group_usv'

weewx.units.USUnits['group_usv'] = 'usv'
weewx.units.MetricUnits['group_usv'] = 'usv'
weewx.units.MetricWXUnits['group_usv'] = 'usv'

weewx.units.default_unit_format_dict['usv'] = '%.1f'
weewx.units.default_unit_label_dict['usv'] = ' µSV'
