

def get_registered_user():
    # return {
    #     "profile_id": "649f7cd4-b792-4040-8368-eddb734c7ad0",
    #     "merchant_id": "1b99bdcf-d582-4f49-9715-1b61dfff3924",
    #     "journey_id": "018b7e14-af96-47ec-b3da-6c084d54e5b7",
    #     "node_id": "f54dbd37-9519-4e04-87a7-954de3286c53",
    #     "event_type": "SENT",
    #     "event_time": 1617853600.9682,
    #     "instance_id": "bc42d471-b7b2-4935-b4c2-43135d4e622a",
    #     "endpoint": "email2@gmail.com"
    # }
    return {
        'lst_field_updated': [
            'social_event'
        ],
        'lst_transaction_event': [],
        'merchant_id': '1b99bdcf-d582-4f49-9715-1b61dfff3924',
        'updated_time': 1616773712.494396,
        'lst_social_event_updated': [
            {
                'profile_id': '0cdc2661-ae86-491a-a09e-cb3d71641b92',
                'profile_group_id': None,
                'action_time_v2': '2020-10-22T04: 58: 52.000000Z',
                'social_value_str': None,
                'classify': 0,
                'page_social_id': '121358061894056',
                'topic_social_id': '121358061894056_628950601134797',
                'hashtag': [],
                'social_action_str': 'FB_comment'
            }
        ],
        'profile_id': '0cdc2661-ae86-491a-a09e-cb3d71641b92'
    }

if __name__ == "__main__":
    print(get_registered_user())
