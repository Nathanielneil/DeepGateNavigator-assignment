import airsimneurips as airsim
airsim_client = airsim.MultirotorClient()
airsim_client.simLoadLevel('ZhangJiaJie_Medium')
#airsim_client.simLoadLevel('Building99_Hard')
#airsim_client.simLoadLevel('Soccer_Field_Easy')
airsim_client.simStartRace(1)