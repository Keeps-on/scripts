data = [{'value': 471, 'title': 'xiao'}, {'value': 1, 'title': 'Administrator'}, {'value': 417, 'title': 'zhao'},
                {'value': 6, 'title': 'yang'}, {'value': 470, 'title': 'lipp'}]


def change_key(d):
        """
            将字典的键更换
                :param d:
                        :return:
                                """
                                    d['id'] = d.pop('value')
                                        d['name'] = d.pop('title')
                                            return d


                                        user_list = map(change_key, data)

                                        print(list(user_list))
                                        
