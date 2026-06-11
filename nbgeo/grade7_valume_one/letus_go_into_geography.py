import rich
def judge_directions_on_maps():
    underlined1 = "[underline green]北[/underline green]"
    underlined2 = "[underline green]南[/underline green]"
    underlined3 = "[underline green]西[/underline green]"
    underlined4 = "[underline green]东[/underline green]"
    underlined5 = "[underline green]北方[/underline green]"
    underlined6 = "[underline green]东西[/underline green]"
    underlined7 = "[underline green]南北[/underline green]"
    normal = f"[green]一般地图：上{underlined1}下{underlined2}，左{underlined3}右{underlined4}[/green]"
    label = f"[green]有指向标的地图：指向标箭头的指向↗为{underlined5}[/green]"
    line = f"[green]经纬线的地图：纬线指示{underlined6}，经线指示{underlined7}[/green]"
    rich.print(normal)
    rich.print(label)
    rich.print(line)

#----------test cases---------#
#judge_directions_on_maps()
