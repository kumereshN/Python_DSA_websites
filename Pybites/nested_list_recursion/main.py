import re

def extract_ipv4(data):
    """
    Given a nested list of data return a list of IPv4 address information that can be extracted
    """

    if not data:
        return data

    def rec(data, res):
        if isinstance(data, str):
            res.append(data)
        
        for ch in data:
            if isinstance(ch, list):
                rec(ch, res)
            else:
                res.append(ch)
        return res
    
    res = rec(data, [])

    # Validation if len of res is less than 5
    # ip_address mask
    if len(res) < 5:
        return []
    elif all(res) == False:
        return []

    res_str = ' '.join(res)

    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_address = re.findall(ip_pattern, res_str)

    mask_pattern = r'mask (\d{1,4})'
    mask_value = re.findall(mask_pattern, res_str)

    return list(zip(ip_address, mask_value))


data_0 = []
data_1 = ['ip']
data_2 = [['ip', 'mask']]
data_3 = [['TEST', ['ip', [None], 'mask', ['24'], 'type', ['ip_mask']], 'id']]
data_4 = ['ip', ['"172.16.0.0"'], 'mask', ['12'], 'type', ['ip_mask']]
data_5 = [['TEST', ['ip', ['"not.an.ip.address"'], 'mask', ['24'], 'type', ['ip_mask']], 'id']]
data_6 = ['TEST', 'parent', [], 'uuid', '"khk-yyas4h-323223-wewe-343er-3434-www"', 'display_name', '"services"', 'IPV4', [['ip', ['"192.168.1.0"'], 'mask', ['24'], 'type', ['ip_mask']], ['ip', ['"10.0.0.0"'], 'mask', ['8'], 'type', ['ip_mask']]]]
data_7 = [['TEST', ['parent', [], 'uuid', ['"khk-yyas4h-323223-wewe-343er-3434-www"'], 'display_name', ['"services"'], 'IPV4', [[['ip', ['"1.1.1.0"'], 'mask', ['20'], 'type', ['ip_mask']], ['ip', ['"2.2.2.2"'], 'mask', ['32'], 'type', ['ip_mask']]]]]]]

print(extract_ipv4(data_6))