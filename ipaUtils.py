import zipfile, plistlib, sys, re, json, chardet, hashlib, base64
from urllib import parse


def analyze_ipa_with_plistlib(ipa_path):
    ipa_file = zipfile.ZipFile(ipa_path)
    plist_path = find_plist_path(ipa_file)
    plist_data = ipa_file.read(plist_path)
    plist_root = plistlib.loads(plist_data)
    print_ipa_info(plist_root)


def find_plist_path(zip_file):
    name_list = zip_file.namelist()
    pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
    for path in name_list:
        m = pattern.match(path)
        if m is not None:
            return m.group()


def print_ipa_info(plist_root):
    print(json.dumps(plist_root))

    print('Display Name: %s' % plist_root['CFBundleDisplayName'])
    print('Bundle Identifier: %s' % plist_root['CFBundleIdentifier'])
    print('Version: %s' % plist_root['CFBundleShortVersionString'])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

if __name__ == '__main__':

    # analyze_ipa_with_plistlib("/Users/iizvv/Desktop/ipa/DaySign.ipa")

    mobileprovision = open("/Users/iizvv/Downloads/embedded.mobileprovision", 'rb').read()
    # pp0zzKdO7G/8pOPWUmTiycjHKyQ=
    # 6/U8DcN0TitsPMyAHP66YfS5/Je9vzw2/YNzrrDCcdM=
    sha1 = hashlib.sha1(mobileprovision).hexdigest()
    print(bytes.fromhex(sha1))
    print(base64.b64encode(bytes.fromhex(sha1)))
