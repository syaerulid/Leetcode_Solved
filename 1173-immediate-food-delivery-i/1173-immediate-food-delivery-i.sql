WITH
mix_delivery
AS
(
    SELECT 
        delivery_id,
        CASE 
            WHEN order_date = customer_pref_delivery_date THEN 'immediate'
            ELSE 'scheduled' 
            END AS preference_order
    FROM Delivery
    GROUP BY delivery_id),

immediate
AS
(
    SELECT
        COUNT(*) AS immediate_count
    FROM mix_delivery
    WHERE preference_order = 'immediate'
),

total
AS
(
    SELECT 
        COUNT(*) AS total_count
    FROM mix_delivery
)

SELECT
    ROUND((immediate_count / total_count) * 100, 2) as immediate_percentage
FROM total
CROSS JOIN immediate
