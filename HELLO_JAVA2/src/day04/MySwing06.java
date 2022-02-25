package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 255, 197);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_mine = new JLabel("나     :");
		lbl_mine.setBounds(12, 13, 57, 15);
		contentPane.add(lbl_mine);
		
		JLabel lbl_com = new JLabel("컴     :");
		lbl_com.setBounds(12, 51, 57, 15);
		contentPane.add(lbl_com);
		
		JLabel lbl_result = new JLabel("결과  :");
		lbl_result.setBounds(12, 90, 57, 15);
		contentPane.add(lbl_result);
		
		tf_mine = new JTextField();
		tf_mine.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				int key = e.getKeyCode();
//				if(key == KeyEvent.VK_ENTER) {
				if(e.getKeyCode() == 10) {
					myClick();
				}
			}
		});
		tf_mine.setBounds(111, 10, 116, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);
		
		tf_com = new JTextField();
		tf_com.setBounds(111, 48, 116, 21);
		contentPane.add(tf_com);
		tf_com.setColumns(10);
		
		tf_result = new JTextField();
		tf_result.setBounds(111, 87, 116, 21);
		contentPane.add(tf_result);
		tf_result.setColumns(10);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(12, 127, 215, 23);
		contentPane.add(btn);
	}
	
	public void myClick() {
//		String mine = tf_mine.getText();
//
//		String[] com = {"홀", "짝"};
//		int rnd = (int)(Math.random() * 2);
//		tf_com.setText(com[rnd]);
//		
//		if(com[rnd].equals(mine)) {
//			tf_result.setText("승리");
//		}else {
//			tf_result.setText("패배");
//		}
		
		String com = "";
		String mine = tf_mine.getText();
		String result = "";
		
		double rnd = Math.random();
		if(rnd > 0.5) {
			com = "홀";
		}else {
			com = "짝";
		}
		
		if(com.equals(mine)) {
			result = "승리";
		}else {
			result = "패배";
		}
		
		tf_com.setText(com);
		tf_result.setText(result);
	}
}
