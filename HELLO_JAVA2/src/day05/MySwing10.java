package day05;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
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
	public MySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 227, 161);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나");
		lblMine.setBounds(12, 10, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴");
		lblCom.setBounds(12, 35, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과");
		lblResult.setBounds(12, 60, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				if(e.getKeyCode() == 10) {
					myClick();
				}
			}
		});
		tfMine.setHorizontalAlignment(SwingConstants.CENTER);
		tfMine.setBounds(81, 7, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setHorizontalAlignment(SwingConstants.CENTER);
		tfCom.setBounds(81, 32, 116, 21);
		contentPane.add(tfCom);
		tfCom.setColumns(10);
		
		tfResult = new JTextField();
		tfResult.setHorizontalAlignment(SwingConstants.CENTER);
		tfResult.setBounds(81, 57, 116, 21);
		contentPane.add(tfResult);
		tfResult.setColumns(10);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(12, 85, 185, 23);
		contentPane.add(btn);
	}
	
	public void myClick() {
		String mine = tfMine.getText();
		int num = (int)(Math.random() * 3) + 1;
		String com = "";
		String result = "";
		
		if(num == 1) {
			com = "가위";
		}else if(num == 2) {
			com = "바위";
		}else {
			com = "보";
		}
		
		if(com.equals(mine)) {
			result = "비김";
		}else if((com.equals("가위") && mine.equals("바위")) || 
				 (com.equals("바위") && mine.equals("보")) || 
				 (com.equals("보") && mine.equals("가위"))) {
			result = "승리";
		}else {
			result = "패배";
		}
		
		tfCom.setText(com);
		tfResult.setText(result);
	}
}
