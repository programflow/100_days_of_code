# Modifying Global Scope


# enemies = "Skeleton"
enemies = 1
def increase_enemies(enemy):
    # enemies = "Zombie"
    # try not to do this
    # global enemies
    # enemies += 1
    print(f"enemies inside function: {enemy}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


