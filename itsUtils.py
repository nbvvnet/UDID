import requestUtils, json, URL

# 注册新设备， token， udid, 设备类型IOS
# return False, 设备注册id
def registerNewDevice(token, udid):
    data = dict(
        data=dict(
            type='devices',
            attributes=dict(
                name=udid,
                udid=udid,
                platform='IOS'
            )
        )
    )
    result = requestUtils.post(token, URL.registerNewDevice, data)
    try:
        id = json.loads(result.content.decode())['data']['id']
    except BaseException:
        return False
    return id

# 注册新包id
# return False, 设备注册id
def registerNewBundleID(token, identifier):
    data = dict(
        data=dict(
            type='bundleIds',
            attributes=dict(
                identifier=identifier,
                name=identifier.replace('.', ''),
                platform='IOS'
            )
        )
    )
    result = requestUtils.post(token, URL.registerNewBundleID, data)
    try:
        id = json.loads(result.content.decode())['data']['id']
    except BaseException:
        return False
    return id

# 创建证书
def createCertificate(token, csrContent):
    data = dict(
        data=dict(
            type='certificates',
            attributes=dict(
                certificateType='IOS_DEVELOPMENT',
                csrContent=csrContent
            ),
        )
    )
    result = requestUtils.post(token, URL.createCertificate, data)
    print(result.text)
    try:
        id = json.loads(result.content.decode())['data']['id']
    except BaseException:
        return False
    return id

# 注册新用户
def registerProfile(token, identifier, udid, certificateID):
    data = dict(
        data=dict(
            type='profiles',
            attributes=dict(
                name='',
                profileType='IOS_APP_ADHOC'
            ),
            relationships=dict(
                bundleId=dict(
                    data=dict(
                        type='bundleIds',
                        id=identifier,
                    )
                ),
                certificates=dict(
                    data=dict(
                        type='certificates',
                        id=certificateID
                    )
                )
            ),
            devices=dict(
                data=dict(
                    type='devices',
                    id=udid
                )
            )
        )
    )
