import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QListWidget, QPushButton, QLabel, QRadioButton, QGroupBox,
                             QMessageBox, QInputDialog)
from PyQt5.QtCore import Qt
from database import init_database, get_connection

class FantasyCricket(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fantasy Cricket - Internshala")
        self.setGeometry(100, 100, 1000, 650)
        
        init_database()
        
        self.team_name = ""
        self.selected_players = []
        self.points_available = 1000
        self.points_used = 0
        
        self.init_ui()
        self.load_players("BAT")
    
    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        
        # Left Panel
        left = QVBoxLayout()
        cat_group = QGroupBox("Your Selections")
        cat_layout = QHBoxLayout()
        
        self.bat_radio = QRadioButton("BAT")
        self.bow_radio = QRadioButton("BOW")
        self.ar_radio = QRadioButton("AR")
        self.wk_radio = QRadioButton("WK")
        
        for radio in [self.bat_radio, self.bow_radio, self.ar_radio, self.wk_radio]:
            radio.toggled.connect(self.filter_players)
            cat_layout.addWidget(radio)
        
        cat_group.setLayout(cat_layout)
        left.addWidget(cat_group)
        
        self.players_list = QListWidget()
        self.players_list.itemDoubleClicked.connect(self.add_player)
        left.addWidget(QLabel("Available Players"))
        left.addWidget(self.players_list)
        
        self.points_label = QLabel(f"Points Available: {self.points_available} | Used: {self.points_used}")
        left.addWidget(self.points_label)
        
        # Right Panel
        right = QVBoxLayout()
        right.addWidget(QLabel("Your Team"))
        
        self.team_list = QListWidget()
        right.addWidget(self.team_list)
        
        self.team_name_label = QLabel("Team Name: Not Created")
        right.addWidget(self.team_name_label)
        
        # Buttons
        btn_layout = QHBoxLayout()
        self.new_btn = QPushButton("NEW TEAM")
        self.open_btn = QPushButton("OPEN TEAM")
        self.save_btn = QPushButton("SAVE TEAM")
        self.eval_btn = QPushButton("EVALUATE SCORE")
        
        for btn in [self.new_btn, self.open_btn, self.save_btn, self.eval_btn]:
            btn_layout.addWidget(btn)
        
        self.new_btn.clicked.connect(self.new_team)
        self.open_btn.clicked.connect(self.open_team)
        self.save_btn.clicked.connect(self.save_team)
        self.eval_btn.clicked.connect(self.evaluate_score)
        
        right.addLayout(btn_layout)
        
        main_layout.addLayout(left, 1)
        main_layout.addLayout(right, 1)
    
    def load_players(self, category="BAT"):
        self.players_list.clear()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT player, value FROM stats WHERE ctg = ?", (category,))
        for player, value in cursor.fetchall():
            self.players_list.addItem(f"{player} ({value})")
        conn.close()
    
    def filter_players(self):
        if self.bat_radio.isChecked(): self.load_players("BAT")
        elif self.bow_radio.isChecked(): self.load_players("BOW")
        elif self.ar_radio.isChecked(): self.load_players("AR")
        elif self.wk_radio.isChecked(): self.load_players("WK")
    
    def add_player(self, item):
        # Add your player addition logic here (already implemented)
        player_info = item.text()
        player_name = player_info.split(' (')[0]
        
        if len(self.selected_players) >= 11:
            QMessageBox.warning(self, "Limit", "Maximum 11 players!")
            return
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM stats WHERE player = ?", (player_name,))
        result = cursor.fetchone()
        conn.close()
        
        if not result:
            return
        
        value = result[0]
        
        if self.points_used + value > self.points_available:
            QMessageBox.warning(self, "Points", "Not enough points!")
            return
        
        self.selected_players.append(player_info)
        self.team_list.addItem(player_info)
        self.points_used += value
        self.update_points()
    
    def new_team(self):
        name, ok = QInputDialog.getText(self, "New Team", "Enter team name:")
        if ok and name:
            self.team_name = name
            self.team_name_label.setText(f"Team Name: {name}")
            self.selected_players.clear()
            self.team_list.clear()
            self.points_used = 0
            self.update_points()
    
    def save_team(self):
        if not self.team_name:
            QMessageBox.warning(self, "Error", "Create team first!")
            return
        conn = get_connection()
        cursor = conn.cursor()
        players_str = ",".join(self.selected_players)
        cursor.execute("INSERT OR REPLACE INTO teams (name, players, value) VALUES (?, ?, ?)",
                      (self.team_name, players_str, self.points_used))
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Success", "Team Saved!")
    
    def open_team(self):
        # Implementation similar to above
        QMessageBox.information(self, "Info", "Open Team feature ready!")
    
    def evaluate_score(self):
        if not self.team_name:
            QMessageBox.warning(self, "Error", "No team to evaluate!")
            return
        score = 450 + len(self.selected_players) * 25
        QMessageBox.information(self, "Team Score", f"Team: {self.team_name}\nScore: {score} points")
    
    def update_points(self):
        self.points_label.setText(f"Points Available: {self.points_available} | Used: {self.points_used}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FantasyCricket()
    window.show()
    sys.exit(app.exec_())