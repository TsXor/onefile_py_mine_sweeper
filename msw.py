import io
from typing import Dict, List, Tuple, Set, Any, Callable

RES_LIST = [
    'img/0.gif',
    'img/1.gif',
    'img/2.gif',
    'img/3.gif',
    'img/4.gif',
    'img/5.gif',
    'img/6.gif',
    'img/7.gif',
    'img/8.gif',
    'img/9.gif',
    'img/10.gif',
    'img/11.gif',
    'img/12.gif',
    'img/13.gif',
    'img/14.gif',
    'img/face1.gif',
    'img/face2.gif',
    'img/face3.gif',
]

RES_IOMAP: Dict[str, io.IOBase] = {}
RES_MISSING: List[Tuple[str, str]] = []

if 'RES_INLINE' in globals():
    RES_INLINE: Dict[str, bytes]
    # 资源已内联
    for res_path in RES_LIST:
        if res_path in RES_INLINE: # type: ignore
            RES_IOMAP[res_path] = io.BytesIO(RES_INLINE[res_path]) # type: ignore
        else:
            RES_MISSING.append((res_path, '内联资源不存在'))
else:
    # 资源未内联
    for res_path in RES_LIST:
        try:
            res_fp = open(res_path, 'rb')
            RES_IOMAP[res_path] = res_fp
        except BaseException as exc:
            RES_MISSING.append((res_path, str(exc)))

if RES_MISSING:
    import tkinter.messagebox as tkmsg
    missing_info = '加载以下资源失败：'
    for info in RES_MISSING:
        missing_info += '\n加载%s失败：%s' % info
    tkmsg.showerror(title='你说得对，但是',
                    message=missing_info)
    exit()
            

import tkinter as tk  # UI界面
import tkinter.messagebox as tkmsg
from PIL import Image, ImageTk
import random  # 随机数
import abc
import numpy as np, numpy.typing as npt
import math, fractions
import time, threading
from functools import partial


# 常量
BUTTON_STATES = {'E', 'M', 'B', 'X', 'F', 1, 2, 3, 4, 5, 6, 7, 8}
BUTTON_STATE_IMAGE_MAP = {
    0:   Image.open(fp=RES_IOMAP['img/0.gif']),   # 空白方块
    1:   Image.open(fp=RES_IOMAP['img/1.gif']),   # 数字1
    2:   Image.open(fp=RES_IOMAP['img/2.gif']),   # 数字2
    3:   Image.open(fp=RES_IOMAP['img/3.gif']),   # 数字3
    4:   Image.open(fp=RES_IOMAP['img/4.gif']),   # 数字4
    5:   Image.open(fp=RES_IOMAP['img/5.gif']),   # 数字5
    6:   Image.open(fp=RES_IOMAP['img/6.gif']),   # 数字6
    7:   Image.open(fp=RES_IOMAP['img/7.gif']),   # 数字7
    8:   Image.open(fp=RES_IOMAP['img/8.gif']),   # 数字8
    'B': Image.open(fp=RES_IOMAP['img/9.gif']),   # 爆炸雷
    'X': Image.open(fp=RES_IOMAP['img/10.gif']),  # 标错雷
    'F': Image.open(fp=RES_IOMAP['img/11.gif']),  # 旗子
    'E': Image.open(fp=RES_IOMAP['img/12.gif']),  # 立体方块
    'M': Image.open(fp=RES_IOMAP['img/13.gif']),  # 未爆炸雷
    'H': Image.open(fp=RES_IOMAP['img/14.gif']),  # 炸弹，作弊模式下使用
}
FACE_STATE_IMAGE_MAP = {
    'in_progress': Image.open(fp=RES_IOMAP['img/face1.gif']),  # 笑脸
    'success':     Image.open(fp=RES_IOMAP['img/face2.gif']),  # 耍酷脸
    'fail':        Image.open(fp=RES_IOMAP['img/face3.gif']),  # 哭脸
}

EASTER_EGG = False
if EASTER_EGG: print('EASTER_EGG = True，开启彩蛋')

def wrap_evt_handler(f: Callable[[], None]) -> Callable[[Any], None]:
    def evt_handler(evt: Any): f()
    return evt_handler


class MyPyMatrix: # 自定义二维数组类
    shape: Tuple[int, int]
    data: List[Any]

    # 注：初始化值应为不可变类型
    def __init__(self, shape: Tuple[int, int], init_val: Any) -> None:
        self.shape = shape
        n_rows, n_cols = shape
        self.data = [init_val] * (n_rows * n_cols)
    
    def get(self, x: int, y: int) -> Any:
        n_rows, n_cols = self.shape
        x_check = x >= 0 and x < n_cols
        y_check = y >= 0 and y < n_rows
        if x_check and y_check:
            return self.data[n_cols * y + x]
        else:
            raise IndexError
    
    # 如果索引越界，返回默认值
    def get_noerr(self, x: int, y: int, default: Any) -> Any:
        try:
            return self.get(x, y)
        except IndexError:
            return default
    
    def set(self, x: int, y: int, val: Any) -> None:
        n_rows, n_cols = self.shape
        x_check = x >= 0 and x < n_cols
        y_check = y >= 0 and y < n_rows
        if x_check and y_check:
            self.data[n_cols * y + x] = val
        else:
            raise IndexError
    
    # 如果索引越界，不做任何事
    def set_noerr(self, x: int, y: int, val: Any) -> None:
        try:
            self.set(x, y, val)
        except IndexError:
            pass
    
    def modify(self, x: int, y: int, modifier: Callable[[Any], Any]) -> None:
        n_rows, n_cols = self.shape
        x_check = x >= 0 and x < n_cols
        y_check = y >= 0 and y < n_rows
        if x_check and y_check:
            self.data[n_cols * y + x] = modifier(self.data[n_cols * y + x])
        else:
            raise IndexError
    
    # 如果索引越界，不做任何事
    def modify_noerr(self, x: int, y: int, modifier: Callable[[Any], Any]) -> None:
        try:
            self.modify(x, y, modifier)
        except IndexError:
            pass
    
    def copy(self):
        obj = MyPyMatrix(self.shape, None)
        obj.data = self.data.copy()
    
    def enumerate(self):
        n_rows, n_cols = self.shape
        for i, e in enumerate(self.data):
            yield (i % n_cols, i // n_cols), e


class MyTimer:
    begin_time: float
    thr_running: bool
    thr: threading.Thread
    tick_interval: float = 0.1
    on_tick: List[Callable[[float], None]]

    def __init__(self) -> None:
        self.on_tick = []
        self.reset()
        self.thr_running = True
        self.thr = threading.Thread(target=self._run, daemon=True)
        self.thr.start()

    def _run(self):
        # 虽然每次执行_tick的间隔是tick_interval
        # 但是由于这并不是RTOS，以及_tick和一系列回调执行本身需要时间
        # 所以tick_interval是最大误差，而不是计时单位
        while True:
            self._tick()
            time.sleep(self.tick_interval)

    def _tick(self):
        t = time.time()
        for f in self.on_tick: f(t - self.begin_time)

    def reset(self):
        self.begin_time = time.time()


class MineState:
    timer: MyTimer
    time_limit: int
    shape: Tuple[int, int] # 场地宽高
    hacked_view: bool # 是否作弊查看所有雷
    first_op_commited: bool # 是否已进行第一次操作
    n_mines: int # 地雷数
    n_success_left: int # 距离成功需要排除的空地数
    n_flags_left: int # 剩余可用标记数
    game_end: bool # 游戏是否结束
    success: bool # 游戏是否胜利
    mine_state_matrix: MyPyMatrix # 是否为雷
    revealed_state_matrix: MyPyMatrix # 是否已探索
    marked_state_matrix: MyPyMatrix # 是否标记
    surrounding_mines_matrix: MyPyMatrix # 周围雷数
    on_game_end: List[Callable[[bool], None]] # 游戏结束回调
    on_update: List[Callable[[Tuple[int, int]], None]] # 地块状态更新回调
    on_reset: List[Callable[[], None]] # 游戏数据重置回调
    on_param_change: List[Callable[[], None]] # 游戏参数重置回调
    on_time_change: List[Callable[[float], None]] # 时间更改回调

    def __init__(self,
        n_rows: int, n_cols: int,
        n_mines: int,
        time_limit: int,
    ) -> None:
        if EASTER_EGG:
            mine_ratio = fractions.Fraction(n_mines, n_rows * n_cols)
            print('数据：场地为%dx%d，共%d个雷，占%s' % (n_cols, n_rows, n_mines, str(mine_ratio)))
        self.time_limit = time_limit
        self.timer = MyTimer()
        self.timer.on_tick.append(self._on_tick)
        self.shape = (n_rows, n_cols)
        self.n_mines = n_mines
        self.on_game_end = []
        self.on_update = []
        self.on_reset = []
        self.on_param_change = []
        self.on_time_change = []
        self.reset_game()
    
    def reset_params(self,
        n_rows: int, n_cols: int,
        n_mines: int,
        time_limit: int,
    ) -> None:
        self.shape = (n_rows, n_cols)
        self.n_mines = n_mines
        self.time_limit = time_limit
        for f in self.on_param_change: f()
        self.reset_game()

    # 每0.1s（不准确）触发
    def _on_tick(self, t: float):
        if not self.first_op_commited:
            self.timer.reset()
        elif not self.game_end:
            # 如果时间限制为不是正数，那么不限时
            if self.time_limit > 0:
                if int(t) > self.time_limit: self._on_game_end(False)
            for f in self.on_time_change: f(t)

    # 只重置地雷数据
    def _reshuffle_mines(self, fix_data=None):
        self.mine_state_matrix = MyPyMatrix(self.shape, 0)
        self.surrounding_mines_matrix = MyPyMatrix(self.shape, 0)
        # 将地雷状态数组的前(地雷数量)个设为1，然后打乱
        if fix_data is None:
            for i in range(self.n_mines):
                self.mine_state_matrix.data[i] = 1
            random.shuffle(self.mine_state_matrix.data)
        else:
            self.mine_state_matrix.data = fix_data
        for (x, y), state in self.mine_state_matrix.enumerate():                
            if state:
                inc = lambda x: x + 1
                # 更新周围雷数
                self.surrounding_mines_matrix.modify_noerr(x - 1, y - 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x - 1, y, inc)
                self.surrounding_mines_matrix.modify_noerr(x - 1, y + 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x, y - 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x, y, inc)
                self.surrounding_mines_matrix.modify_noerr(x, y + 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x + 1, y - 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x + 1, y, inc)
                self.surrounding_mines_matrix.modify_noerr(x + 1, y + 1, inc)

    # 重置游戏数据
    def reset_game(self):
        self.first_op_commited = False
        self.hacked_view = False
        n_rows, n_cols = self.shape
        self.game_end = False
        self.success = False
        self.n_success_left = n_rows * n_cols - self.n_mines
        self.n_flags_left = self.n_mines
        self.revealed_state_matrix = MyPyMatrix(self.shape, False)
        self.marked_state_matrix = MyPyMatrix(self.shape, False)
        self._reshuffle_mines()
        for f in self.on_reset: f()

    # 探索某位置
    def reveal(self, pos: Tuple[int, int]):
        if self.game_end: return
        # 如果标记过，探索无效
        if self.marked_state_matrix.get(*pos): return
        # 如果该位置已探索，探索无效
        if self.revealed_state_matrix.get(*pos): return
        # 如果首次探索，保证探索点不是雷且触发扩展探索
        if not self.first_op_commited:
            self.first_op_commited = True
            n_auto_remake = 0
            while self.mine_state_matrix.get(*pos) \
               or self.surrounding_mines_matrix.get(*pos) != 0:
                self._reshuffle_mines()
                n_auto_remake += 1
            if EASTER_EGG:
                print('你知道吗？系统为你自动重开了%d次，每次开局都是一种幸运。'
                      % n_auto_remake)
        
        # 探索主流程
        self.revealed_state_matrix.set(*pos, True)
        for f in self.on_update: f(pos)
        if self.mine_state_matrix.get(*pos):
            self._on_game_end(False)
        else:
            self.n_success_left -= 1
            if self.surrounding_mines_matrix.get(*pos) == 0:
                # 空格，扩展探索
                explored = set([pos])
                for npos in self._get_surrounding_pos(pos):
                    self._reveal_expand(npos, explored)
            if self.n_success_left <= 0: # 正常情况下不可能小于0，兜个底
                self._on_game_end(True)
    
    def _get_surrounding_pos(self, pos: Tuple[int, int]):
        x, y = pos; n_rows, n_cols = self.shape
        for ny in range(max(y-1, 0), min(y+1+1, n_rows)):
            for nx in range(max(x-1, 0), min(x+1+1, n_cols)):
                if not (ny == y and nx == x): yield (nx, ny)
    
    # 扩展探索直到遇到周围雷数不为0或有雷的格
    def _reveal_expand(self, pos: Tuple[int, int], explored: Set[Tuple[int, int]]):
        if pos in explored: return
        explored.add(pos)
        if self.mine_state_matrix.get(*pos): return
        # 如果未标记且未探索，记为已探索
        if not self.marked_state_matrix.get(*pos) and \
           not self.revealed_state_matrix.get(*pos):
            self.revealed_state_matrix.set(*pos, True)
            for f in self.on_update: f(pos)
            self.n_success_left -= 1
        if self.surrounding_mines_matrix.get(*pos) != 0: return
        for npos in self._get_surrounding_pos(pos):
            self._reveal_expand(npos, explored)

    # 标记某位置
    def mark(self, pos: Tuple[int, int]):
        if self.game_end: return
        # 如果该位置已探索，标记无效
        if self.revealed_state_matrix.get(*pos): return
        
        # 标记主流程
        if self.marked_state_matrix.get(*pos):
            # 取消标记
            self.n_flags_left += 1
        else:
            # 标记
            # 如果没有多余的标记限额，标记无效
            if self.n_flags_left == 0: return
            self.n_flags_left -= 1
        self.marked_state_matrix.modify(*pos, lambda x: not x)
        for f in self.on_update: f(pos)
    
    # 作弊，如果是雷则标记，不是则探索
    def hack_alright(self, pos: Tuple[int, int]):
        if self.marked_state_matrix.get(*pos):
            self.mark(pos) # 取消标记
        if self.mine_state_matrix.get(*pos) and self.first_op_commited:
            self.mark(pos)
        else:
            self.reveal(pos)
    
    # 作弊，显示所有雷
    def hack_viewall(self):
        if not self.first_op_commited: return
        self.hacked_view = not self.hacked_view
        for pos, is_mine in self.mine_state_matrix.enumerate():
            if is_mine:
                for f in self.on_update: f(pos)
    
    # 作弊，自动通关
    def hack_complete(self):
        self.hack_alright(self.get_rand_pos())
        for pos, is_mine in self.mine_state_matrix.enumerate():
            self.hack_alright(pos)

    # 游戏结束时触发
    def _on_game_end(self, success: bool):
        self.game_end = True
        self.success = success
        for f in self.on_game_end: f(success)
    
    # 强制结束游戏
    def force_end(self, success: bool):
        self._on_game_end(success)
    
    def get_rand_pos(self):
        n_rows, n_cols = self.shape
        rx = random.randint(0, n_cols-1)
        ry = random.randint(0, n_rows-1)
        return (rx, ry)


class ButtonField:
    tk_frame: tk.Frame
    game_state: MineState
    buttons_matrix: MyPyMatrix # 按钮
    button_size: int
    button_state_image_map: Dict[Any, ImageTk.PhotoImage]

    @property
    def tk_obj(self): return self.tk_frame

    def __init__(self,
        master,
        game_state: MineState,
        button_size: int
    ) -> None:
        self.button_state_image_map = {k: ImageTk.PhotoImage(v.resize((button_size, button_size)))
                                       for k, v in BUTTON_STATE_IMAGE_MAP.items()}
        self.game_state = game_state
        self.game_state.on_update.append(self._on_update)
        self.game_state.on_game_end.append(self._on_game_end)
        self.game_state.on_reset.append(self._reset_buttons)
        self.game_state.on_param_change.append(self._on_reset_params)
        
        self.button_size = button_size
        self.tk_frame = tk.Frame(master=master)
        self.tk_frame.pack_propagate(False)
        self._init_buttons()
        self._reset_buttons()

    def _init_buttons(self): # 初始化按钮
        n_rows, n_cols = self.game_state.shape
        self.tk_frame.configure(width=n_cols*self.button_size, height=n_rows*self.button_size)
        self.buttons_matrix = MyPyMatrix(self.game_state.shape, None)
        for y in range(n_rows):
            for x in range(n_cols):
                btn = tk.Button(master=self.tk_frame)
                btn.bind(sequence="<Button-1>", func=wrap_evt_handler(partial(self.game_state.reveal, (x, y))))
                btn.bind(sequence="<Button-2>", func=wrap_evt_handler(partial(self.game_state.hack_alright, (x, y))))
                btn.bind(sequence="<Button-3>", func=wrap_evt_handler(partial(self.game_state.mark, (x, y))))
                btn.place(
                    width=self.button_size, height=self.button_size,
                    x=(x*self.button_size), y=(y*self.button_size)
                )
                self.buttons_matrix.set(x, y, btn)
    
    def _on_reset_params(self): # 重置UI状态
        btn: tk.Button
        for btn in self.buttons_matrix.data:
            btn.destroy()
        self.buttons_matrix.data.clear()
        self._init_buttons()
    
    def _reset_buttons(self): # 重置按钮状态
        btn: tk.Button
        for btn in self.buttons_matrix.data:
            btn.config(image=self.button_state_image_map['E'])

    # 某位置状态更新时触发
    def _on_update(self, button_pos: Tuple[int, int]):
        x, y = button_pos
        self.buttons_matrix.get(x, y).config(
            image=self.button_state_image_map[self._decide_button_state(x, y)]
        )
    
    # 游戏结束时触发
    def _on_game_end(self, success: bool):
        for (x, y), revealed in self.game_state.revealed_state_matrix.enumerate():
            if not revealed:
                self.buttons_matrix.get(x, y).config(
                    image=self.button_state_image_map[self._decide_final_state(x, y)]
                )

    # 决定按钮如何显示
    def _decide_button_state(self, x: int, y: int):
        if not self.game_state.revealed_state_matrix.get(x, y): # 未探索
            if self.game_state.hacked_view and self.game_state.mine_state_matrix.get(x, y):
                return 'H'
            elif self.game_state.marked_state_matrix.get(x, y): # 已标记
                return 'F'
            else: # 未标记
                return 'E'
        else: # 已探索
            if self.game_state.mine_state_matrix.get(x, y): # 是雷
                return 'B'
            else: # 不是雷
                return self.game_state.surrounding_mines_matrix.get(x, y)
    
    # 决定游戏结束后未探索的按钮如何显示
    def _decide_final_state(self, x: int, y: int):
        if self.game_state.mine_state_matrix.get(x, y): # 是雷
            return 'M'
        else: # 不是雷
            if self.game_state.marked_state_matrix.get(x, y): # 已标记
                return 'X'
            else: # 未标记
                return 'E'


class StatusHeader:
    tk_frame: tk.Frame
    game_state: MineState
    face_btn: tk.Button
    n_flags_label: tk.Label
    time_used_label: tk.Label
    face_button_size: int
    field_button_size: int
    face_state_image_map: Dict[Any, ImageTk.PhotoImage]

    @property
    def tk_obj(self): return self.tk_frame

    def __init__(self,
        master,
        game_state: MineState,
        face_button_size: int,
        field_button_size: int
    ) -> None:
        self.face_state_image_map = {k: ImageTk.PhotoImage(v.resize((face_button_size, face_button_size)))
                                     for k, v in FACE_STATE_IMAGE_MAP.items()}
        self.game_state = game_state
        self.game_state.on_update.append(self._on_update)
        self.game_state.on_game_end.append(self._on_game_end)
        self.game_state.on_reset.append(self._reset_ui)
        self.game_state.on_param_change.append(self._set_width)
        self.game_state.on_time_change.append(self._on_time_change)
        
        self.face_button_size = face_button_size
        self.field_button_size = field_button_size
        self.tk_frame = tk.Frame(master=master, bg='white', relief="sunken")
        self.face_btn = tk.Button(self.tk_frame, relief='raised')
        self.face_btn.bind(sequence="<Button-1>", func=wrap_evt_handler(self.game_state.reset_game))
        self.face_btn.bind(sequence="<Button-2>", func=wrap_evt_handler(self.game_state.hack_complete))
        self.face_btn.bind(sequence="<Button-3>", func=wrap_evt_handler(self.game_state.hack_viewall))
        self.n_flags_label = tk.Label(self.tk_frame, bg='white', fg='red', font=('幼圆', 22))
        self.time_used_label = tk.Label(self.tk_frame, bg='white', fg='red', font=('幼圆', 22))
        
        self.tk_frame.pack_propagate(False)
        self._set_width()
        self._reset_ui()
    
    def _reset_ui(self):
        self.face_btn.config(image=self.face_state_image_map['in_progress'])
        self.n_flags_label.config(text=str(self.game_state.n_flags_left))
        self.time_used_label.config(text='0')
    
    def _set_width(self):
        width = max(self.field_button_size * self.game_state.shape[1], 9 * self.face_button_size)
        self.tk_frame.config(width=width, height=self.face_button_size)
        self.face_btn.place(relx=0.5, rely=0.5, anchor='center',
                            width=self.face_button_size, height=self.face_button_size)
        self.n_flags_label.place(relx=0.0, rely=0.5, x=self.face_button_size, anchor='center',
                                 width=self.face_button_size*2, height=self.face_button_size)
        self.time_used_label.place(relx=1.0, rely=0.5, x=-self.face_button_size*2, anchor='center',
                                   width=self.face_button_size*4, height=self.face_button_size)

    # 某位置状态更新时触发
    def _on_update(self, button_pos: Tuple[int, int]):
        self.n_flags_label.config(text=str(self.game_state.n_flags_left))
    
    # 游戏结束时触发
    def _on_game_end(self, success: bool):
        status = 'success' if success else 'fail'
        self.face_btn.config(image=self.face_state_image_map[status])
    
    # 游戏进行中每0.1s（不准确）触发
    def _on_time_change(self, t: float):
        if self.game_state.time_limit <= 0:
            self.time_used_label.config(text='%d' % int(t))
        else:
            self.time_used_label.config(text='%d/%d' % (int(t), self.game_state.time_limit))
    

class ParamPanel:
    tk_frame: tk.Frame
    time_limit_checkbox_bvar: tk.BooleanVar
    auto_sweeper_hack_checkbox_bvar: tk.BooleanVar
    game_state: MineState
    automata: 'AutoMineSweeper'

    @property
    def tk_obj(self): return self.tk_frame

    def __init__(self, master, game_state: MineState) -> None:
        self.game_state = game_state
        self.automata = EqSolverSweeper(self.game_state)

        # 由pygubu根据可视化设计生成
        self.tk_frame = tk.Frame(master)
        self.n_rows_label = tk.Label(self.tk_frame)
        self.n_rows_label.configure(text="行数")
        self.n_rows_label.grid(column=0, columnspan=2, row=0)
        self.n_rows_input = tk.Entry(self.tk_frame)
        self.n_rows_input.grid(column=2, row=0)
        self.n_cols_label = tk.Label(self.tk_frame)
        self.n_cols_label.configure(text="列数")
        self.n_cols_label.grid(column=0, columnspan=2, row=1)
        self.n_cols_input = tk.Entry(self.tk_frame)
        self.n_cols_input.grid(column=2, row=1)
        self.n_mines_label = tk.Label(self.tk_frame)
        self.n_mines_label.configure(text="地雷数")
        self.n_mines_label.grid(column=0, columnspan=2, row=2)
        self.n_mines_input = tk.Entry(self.tk_frame)
        self.n_mines_input.grid(column=2, row=2)
        self.time_limit_label = tk.Label(self.tk_frame)
        self.time_limit_label.configure(text="时间限制")
        self.time_limit_label.grid(column=0, row=3)
        self.time_limit_checkbox_bvar = tk.BooleanVar()
        self.time_limit_checkbox = tk.Checkbutton(self.tk_frame,
                                   variable=self.time_limit_checkbox_bvar,
                                   command=self._set_time_limit_input_state)
        self.time_limit_checkbox.grid(column=1, row=3)
        self.time_limit_input = tk.Entry(self.tk_frame)
        self.time_limit_input.grid(column=2, row=3)
        self.reminder_label = tk.Label(self.tk_frame)
        self.reminder_label.configure(text='\n'.join([
            "时间限制<=0表示不限时",
            "重置UI延迟较高，保存更改后请耐心等待",
        ]))
        self.reminder_label.grid(column=0, columnspan=3, row=4)
        self.submit_button = tk.Button(self.tk_frame,
                                       command=self.dump_data)
        self.submit_button.configure(text="保存更改并重置游戏")
        self.submit_button.grid(column=0, columnspan=3, row=5)
        self.hack_hint_label = tk.Label(self.tk_frame)
        self.hack_hint_label.configure(text='\n'.join([
            "关于作弊：",
            "雷是完全随机打乱的，所以死局很正常",
            "对某地块点中键，做出必然正确的选择",
            "对笑脸按钮点中键直接通关",
            "对笑脸按钮点右键显示所有雷的位置",
        ]))
        self.hack_hint_label.grid(column=0, columnspan=3, row=6)
        self.auto_sweeper_frame = tk.Frame(self.tk_frame)
        self.auto_sweeper_frame.configure(height=200, width=200)
        self.auto_sweeper_button = tk.Button(self.auto_sweeper_frame,
                                             command=self.automata)
        self.auto_sweeper_button.configure(text="自动扫雷")
        self.auto_sweeper_button.pack(side="left")
        self.auto_sweeper_hack_checkbox_bvar = tk.BooleanVar()
        self.auto_sweeper_hack_checkbox = tk.Checkbutton(self.auto_sweeper_frame,
                                          variable=self.auto_sweeper_hack_checkbox_bvar,
                                          command=self._set_automata_hack)
        self.auto_sweeper_hack_checkbox.configure(text="不失败")
        self.auto_sweeper_hack_checkbox.pack(side="top")
        self.auto_sweeper_frame.grid(column=0, columnspan=3, row=7)
        self.tk_frame.grid_anchor("center")
        self.load_data()
    
    def _set_automata_hack(self):
        self.automata.use_hack = self.auto_sweeper_hack_checkbox_bvar.get()
    
    def _set_time_limit_input_state(self):
        use_time_limit = self.time_limit_checkbox_bvar.get()
        self.time_limit_input.config(state=('normal' if use_time_limit else 'disabled'))
    
    def dump_data(self):
        try:
            n_rows = int(self.n_rows_input.get())
            n_cols = int(self.n_cols_input.get())
            n_mines = int(self.n_mines_input.get())
            use_time_limit = self.time_limit_checkbox_bvar.get()
            time_limit_str = self.time_limit_input.get()
            time_limit = int(time_limit_str) if use_time_limit else 0
            self.game_state.reset_params(n_rows, n_cols, n_mines, time_limit)
        except:
            tkmsg.showerror(title='你说得对，但是',
                            message='输入值转换错误，请检查您的输入')
    
    def load_data(self):
        n_rows, n_cols = self.game_state.shape
        self.n_rows_input.delete(0, "end")
        self.n_rows_input.insert(0, str(n_rows))
        self.n_cols_input.delete(0, "end")
        self.n_cols_input.insert(0, str(n_cols))
        self.n_mines_input.delete(0, "end")
        self.n_mines_input.insert(0, str(self.game_state.n_mines))
        if self.game_state.time_limit <= 0:
            self.time_limit_checkbox_bvar.set(False)
            self.time_limit_input.delete(0, "end")
            self.time_limit_input.insert(0, str(0))
        else:
            self.time_limit_checkbox_bvar.set(True)
            self.time_limit_input.delete(0, "end")
            self.time_limit_input.insert(0, str(self.game_state.time_limit))


class MineSweeperUI:
    tk_frame: tk.Frame
    subframe_left: tk.Frame
    game_state: MineState
    status_header: StatusHeader
    button_field: ButtonField
    param_panel: ParamPanel

    @property
    def tk_obj(self): return self.tk_frame
    
    def __init__(self,
        master,
        n_rows: int, n_cols: int,
        n_mines: int,
        time_limit: int,
        field_button_size: int,
        face_button_size: int,
    ) -> None:
        self.game_state = MineState(n_rows, n_cols, n_mines, time_limit)
        self.tk_frame = tk.Frame(master=master)
        self.subframe_left = tk.Frame(master=self.tk_frame)
        self.status_header = StatusHeader(self.subframe_left, self.game_state,
                                          face_button_size, field_button_size)
        self.status_header.tk_obj.pack(side='top')
        self.button_field = ButtonField(self.subframe_left, self.game_state, field_button_size)
        self.button_field.tk_obj.pack(side='top')
        self.param_panel = ParamPanel(self.tk_frame, self.game_state)
        self.subframe_left.pack(side='left')
        self.param_panel.tk_obj.pack(side='left')


class MainWin:
    FIELD_BUTTON_SIZE = 20 # 扫雷场地按钮大小
    FACE_BUTTON_SIZE = 40 # 笑脸按钮大小

    def __init__(self,
        n_rows: int, n_cols: int,
        n_mines: int,
        time_limit: int,
    ) -> None:
        self.root = tk.Tk()
        self.root.title('扫雷')
        self.ui = MineSweeperUI(self.root, n_rows, n_cols, n_mines, time_limit,
                                self.FIELD_BUTTON_SIZE, self.FACE_BUTTON_SIZE)
        self.ui.tk_obj.pack()
        self.root.resizable(width=False, height=False)


# 冷知识：扫雷是NP-Complete问题
class AutoMineSweeper(abc.ABC):
    game: MineState
    use_hack: bool
    thr: threading.Thread

    def __init__(self, game: MineState, use_hack: bool = False) -> None:
        self.game = game
        self.use_hack = use_hack
        self.thr = threading.Thread(target=self.run)
    
    def reveal(self, pos: Tuple[int, int]):
        if self.use_hack:
            self.game.hack_alright(pos)
        else:
            self.game.reveal(pos)
    
    @abc.abstractmethod
    def run(self): pass
    
    def __call__(self):
        if self.game.game_end: return
        if not self.thr.is_alive():
            if self.thr.ident is not None:
                self.thr = threading.Thread(target=self.run)
            self.thr.start()


class BogoSweeper(AutoMineSweeper):
    '''
    完全随机地探索地块直到游戏结束
    这个Bogo是猴子排序(Bogo Sort)的那个Bogo
    '''
    def run(self):
        while not self.game.game_end:
            self.reveal(self.game.get_rand_pos())


class EqSolverSweeper(AutoMineSweeper):
    '''
    将扫雷场地的一部分当做方程求解
    时间复杂度很高，也不能保证一定赢(事实上几乎赢不了)
    而且有时候还会卡死
    '''
    # 暴力尝试不定方程的所有01解，O(2^n)
    def solve_bruteforce(self, unknown_coeff_mat: npt.NDArray, n_mines: npt.NDArray):
        results: List[int] = []
        n_rows, n_cols = unknown_coeff_mat.shape
        for bitmask in range(2 ** n_cols):
            bitmask_left = bitmask
            result = np.zeros_like(n_mines); col = 0
            while bitmask_left:
                if bitmask_left & 1: result += unknown_coeff_mat[:, col]
                col += 1; bitmask_left >>= 1
            if np.array_equal(result, n_mines): results.append(bitmask)
        return results
    
    def is_known_point(self, pos: Tuple[int, int]):
        return self.game.revealed_state_matrix.get(*pos) \
           and self.game.surrounding_mines_matrix.get(*pos)

    # 随机得已探索且周围雷数不为0的起始点
    def get_start_point(self):
        valid_pos = False
        while not (valid_pos):
            start_point = self.game.get_rand_pos()
            valid_pos = self.is_known_point(start_point)
        return start_point # type: ignore
    
    # 选择随机已知点周围的已知点建立方程
    def collect_unknown(self):
        knowns = False
        while not knowns:
            pos = self.get_start_point()
            knowns = {p for p in self.game._get_surrounding_pos(pos)
                      if self.is_known_point(p)}
        knowns.add(pos) # type: ignore
        unknowns = {}
        for kpos in knowns:
            for spos in self.game._get_surrounding_pos(kpos):
                if not self.game.revealed_state_matrix.get(*spos):
                    unknowns[spos] = 0
        for i, k in enumerate(unknowns):
            unknowns[k] = i
        unknown_coeff_mat = np.zeros((len(knowns), len(unknowns)), np.uint8)
        n_mines = np.ndarray((len(knowns),), np.uint8)
        for i, kpos in enumerate(knowns):
            n_mines[i] = self.game.surrounding_mines_matrix.get(*kpos)
            for spos in self.game._get_surrounding_pos(kpos):
                if not self.game.revealed_state_matrix.get(*spos):
                    unknown_coeff_mat[i, unknowns[spos]] = 1
        return unknown_coeff_mat, n_mines, unknowns

    def run(self):
        get_bit = lambda x, n: (x >> n) & 1
        if not self.game.first_op_commited:
            self.reveal(self.game.get_rand_pos())
        while not self.game.game_end:
            unknown_coeff_mat, n_mines, unknowns = self.collect_unknown()
            results = self.solve_bruteforce(unknown_coeff_mat, n_mines)
            chosen = random.choice(results)
            for pos, i in unknowns.items():
                if not get_bit(chosen, i):
                    self.reveal(pos)


if __name__ == '__main__':
    main = MainWin(20, 20, 96, 2 * 60)
    main.root.mainloop()
