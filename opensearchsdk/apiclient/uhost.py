from opensearchsdk.apiclient import base


class UhostManager(base.Manager):
    '''
    host manager class
    '''

    def create(self, region, imageid, loginmode, password=None, keypair=None,
               cpu=None, memory=None, diskspace=None, name=None,
               networkid=None, securitygroupid=None, chargetype=None,
               quantity=None):
        '''
        boot an instance
        :param region:
        :param imageid:
        :param loginmode:
        :param password:
        :param keypair:
        :param cpu:
        :param memory:
        :param diskspace:
        :param name:
        :param networkid:
        :param securitygroupid:
        :param chargetype:
        :param quantity:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'CreateUHostInstance'
        body['ImageId'] = imageid
        body['LoginMode'] = loginmode
        if password:
            body['Password'] = password
        if keypair:
            body['KeyPair'] = keypair
        if cpu:
            body['CPU'] = cpu
        if memory:
            body['Memory'] = memory
        if diskspace:
            body['DiskSpace'] = diskspace
        if name:
            body['name'] = name
        if networkid:
            body['NetworkId'] = networkid
        if securitygroupid:
            body['SecuriGroupId'] = securitygroupid
        if chargetype:
            body['ChargeType'] = chargetype
        if quantity:
            body['Quantity'] = quantity

        return self._get(body)

    def get(self, region, uhostid):
        '''
        query host in given region or given host id
        :param region:
        :param uhostid
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = "DescribeUHostInstance"
        body['UHostId'] = uhostid

        return self._get(body)

    def list(self, region, offset=None, limit=None):
        '''
        query host in given region or given host id
        :param region:
        :param offset:
        :param limit:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = "DescribeUHostInstance"
        if offset:
            body['Offset'] = offset
        if limit:
            body['Limit'] = limit

        return self._get(body)

    def terminate(self, region, uhostid):
        '''
        terminate a host
        :param region:
        :param uhostid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'TerminateUHostInstance'
        body['UHostId'] = uhostid

        return self._get(body)

    def resize(self, region, uhostid, cpu, memory, diskspace):
        '''
        resize an instance
        :param region:
        :param uhostid:
        :param cpu:
        :param memory:
        :param diskspace:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'ResizeUHostInstance'
        body['UHostId'] = uhostid
        if cpu:
            body['CPU'] = cpu
        if memory:
            body['Memory'] = memory
        if diskspace:
            body['DiskSpace'] = diskspace

        return self._get(body)

    def reinstall(self, region, uhostid, password=None, imageid=None,
                  reservedisk=None):
        '''
        reinstall an instance
        :param region:
        :param uhostid:
        :param password:
        :param imageid:
        :param reservedisk:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'ReinstallUHostInstance'
        body['UHostId'] = uhostid
        if password:
            body['Password'] = password
        if imageid:
            body['ImageId'] = imageid
        if reservedisk:
            body['ReserveDisk'] = reservedisk

        return self._get(body)

    def start(self, region, uhostid):
        '''
        start an instance
        :param region:
        :param uhostid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['UHostId'] = uhostid
        body['Action'] = 'StartUHostInstance'

        return self._get(body)

    def stop(self, region, uhostid):
        '''
        stop an instance
        :param region:
        :param uhostid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['UHostId'] = uhostid
        body['Action'] = 'StopUHostInstance'

        return self._get(body)

    def reboot(self, region, uhostid):
        '''
        reboot an instance
        :param region:
        :param uhostid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['UHostId'] = uhostid
        body['Action'] = 'RebootUHostInstance'

        return self._get(body)

    def reset_password(self, region, uhostid, password):
        '''
        reset password of an given instance
        :param region:
        :param uhostid:
        :param password:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'ResetUHostInstancePassword'
        body['UHostId'] = uhostid
        body['Password'] = password

        return self._get(body)

    def modify_name(self, region, uhostid, name):
        '''
        modify name of an given instance
        :param region:
        :param uhostid:
        :param name:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'ModifyUHostInstanceName'
        body['UHostId'] = uhostid
        body['Name'] = name

        return self._get(body)

    def modify_tag(self, region, uhostid, tag):
        '''
        modify tag of an given instance
        :param region:
        :param uhostid:
        :param tag:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'ModifyUHostInstanceTag'
        body['UHostId'] = uhostid
        body['Tag'] = tag

        return self._get(body)

    def get_price(self, region, imageid, cpu, memory, count, charge_type=None,
                  disk_space=None):
        '''
        get price of the given configuration instance
        :param region:
        :param imageid:
        :param cpu:
        :param memory:
        :param count:
        :param charge_type:
        :param disk_space:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'GetUHostInstancePrice'
        body['ImageId'] = imageid
        body['CPU'] = cpu
        body['Memory'] = memory
        body['Count'] = count
        if charge_type:
            body['ChargeType'] = charge_type
        if disk_space:
            body['DiskSpace'] = disk_space

        return self._get(body)

    def get_vnc(self, region, uhostid):
        '''
        get vnc info for a given instance
        :param region:
        :param uhostid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['UHostId'] = uhostid
        body['Action'] = 'GetUHostInstanceVncInfo'

        return self._get(body)

    def get_image(self, region, image_type=None, os_type=None, image_id=None,
                  offset=None, limit=None):
        '''
        get image info
        :param region:
        :param image_type:
        :param os_type:
        :param image_id:
        :param offset:
        :param limit:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'DescribeImage'
        if image_type:
            body['ImageType'] = image_type
        if os_type:
            body['OsType'] = os_type
        if image_id:
            body['ImageId'] = image_id
        if offset:
            body['Offset'] = offset
        if limit:
            body['Limit'] = limit

        return self._get(body)

    def create_image(self, region, uhostid, image_name,
                     image_description=None):
        '''
        create by given instance
        :param region:
        :param uhostid:
        :param image_name:
        :param image_description:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'CreateCustomImage'
        body['UHostId'] = uhostid
        body['ImageName'] = image_name
        if image_description:
            body['ImageDescription'] = image_description

        return self._get(body)

    def delete_image(self, region, imageid):
        '''
        delete custom image
        :param region:
        :param imageid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'TerminateCustomImage'
        body['ImageId'] = imageid

        return self._get(body)

    def attach_disk(self, region, uhostid, udiskid):
        '''
        attach a disk to an instance
        :param region:
        :param uhostid:
        :param udiskid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'AttachUDisk'
        body['UHostId'] = uhostid
        body['UDiskId'] = udiskid

        return self._get(body)

    def detach_disk(self, region, uhostid, udiskid):
        '''
        detach a disk from an instance
        :param region:
        :param uhostid:
        :param udiskid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['Action'] = 'DetachUDisk'
        body['UHostId'] = uhostid
        body['UDiskId'] = udiskid

        return self._get(body)

    def create_snapshot(self, region, uhostid):
        '''
        take a snapshot of an instance
        :param region:
        :param uhostid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['UHostId'] = uhostid
        body['Action'] = 'CreateUHostInstanceSnapshot'

        return self._get(body)

    def list_snapshot(self, region, uhostid):
        '''
        list snapshot of an instance
        :param region:
        :param uhostid:
        :return:
        '''
        body = {}
        body['Region'] = region
        body['UHostId'] = uhostid
        body['Action'] = 'DescribeUHostInstanceSnapshot'

        return self._get(body)
