-- 코드를 입력하세요
SELECT CART_ID FROM CART_PRODUCTS
WHERE NAME IN ('MILK', 'YOGURT')
GROUP BY CART_ID
HAVING GROUP_CONCAT(NAME) LIKE '%MILK%' AND GROUP_CONCAT(NAME) LIKE '%YOGURT%'
ORDER BY CART_ID























# SELECT CART_ID
# FROM CART_PRODUCTS
# WHERE NAME IN ('MILK', 'YOGURT')
# GROUP BY CART_ID
# HAVING GROUP_CONCAT(NAME) LIKE '%MILK%' AND GROUP_CONCAT(NAME) LIKE '%YOGURT%'
# ORDER BY CART_ID