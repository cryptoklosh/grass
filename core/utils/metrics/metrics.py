from prometheus_client import Counter, Gauge, Info

grass_info = Info("grass", "Info about grass node")
mined_grass_counter = Counter('mined_grass', 'Times grass was mined', ['account'])
available_proxies_gauge = Gauge('available_proxies', 'Number of available proxies', ['account'])
proxy_score_gauge = Gauge('proxy_score', 'Proxy score', ['account'])
grass_accounts_created_gauge = Gauge('grass_accounts_created', 'Amount of jobs created per account', ['account'])
grass_accounts_active_gauge = Gauge('grass_accounts_active', 'Amount of jobs being actively farmed per account', ['account'])