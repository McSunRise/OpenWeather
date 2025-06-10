from django.core.cache import cache
from django.test import TestCase
from django.core.cache.backends.base import InvalidCacheBackendError


class RedisCacheConnectionTest(TestCase):
    def test_redis_cache_connection(self):
        try:
            cache.set('redis_test_key', 'connected', timeout=5)
            value = cache.get('redis_test_key')
            self.assertEqual(value, 'connected', "Redis не возвращает ожидаемое значение")
        except (ConnectionError, InvalidCacheBackendError) as e:
            self.fail(f"Redis не подключён или произошла ошибка при доступе к кэшу: {e}")
