blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

trending_count = 0
for views in blog_views:
    if views > 1000:
        print("Trending")
        trending_count += 1
    elif 500 <= views <= 1000:
        print("Average")
    else:
        print("Low Traffic")

total_views = sum(blog_views)

print("Total views:", total_views)
print("Number of Trending posts:", trending_count)
