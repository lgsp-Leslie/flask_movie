/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : localhost:3306
 Source Schema         : flask_movie

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 21/05/2021 18:04:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '管理员id',
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '管理员账号',
  `password` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `is_super` smallint(6) NULL DEFAULT NULL COMMENT '是否为超级管理员,0代表超级管理员',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `updated_at` datetime(0) NULL DEFAULT NULL COMMENT '最后登录时间',
  `role_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  INDEX `ix_admin_created_at`(`created_at`) USING BTREE,
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'admin', 'pbkdf2:sha256:150000$pgWUwGJP$9807971b8978d1a2b7fda64327ee36671981bbcc5e6a6110ac5742c173739aea', 0, '2021-05-08 11:59:43', '2021-05-15 16:07:57', 1);

-- ----------------------------
-- Table structure for admin_log
-- ----------------------------
DROP TABLE IF EXISTS `admin_log`;
CREATE TABLE `admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '日志id',
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '管理员用户名',
  `ip` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '登录ip',
  `ua` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'user-agent',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '登录时间',
  `admin_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `admin_id`(`admin_id`) USING BTREE,
  INDEX `ix_admin_log_created_at`(`created_at`) USING BTREE,
  CONSTRAINT `admin_log_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_log
-- ----------------------------
INSERT INTO `admin_log` VALUES (1, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-15 18:00:50', 1);
INSERT INTO `admin_log` VALUES (2, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-16 11:51:22', 1);
INSERT INTO `admin_log` VALUES (3, 'ad', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-16 17:43:57', NULL);
INSERT INTO `admin_log` VALUES (4, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-17 13:10:07', 1);
INSERT INTO `admin_log` VALUES (5, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-18 10:01:51', 1);
INSERT INTO `admin_log` VALUES (6, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-18 10:01:51', 1);
INSERT INTO `admin_log` VALUES (7, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '2021-05-19 11:30:01', 1);

-- ----------------------------
-- Table structure for admin_operate_log
-- ----------------------------
DROP TABLE IF EXISTS `admin_operate_log`;
CREATE TABLE `admin_operate_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '日志id',
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '管理员用户名',
  `ip` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '登录ip',
  `ua` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'user-agent',
  `reason` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '操作原因',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '登录时间',
  `admin_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `admin_id`(`admin_id`) USING BTREE,
  INDEX `ix_admin_operate_log_created_at`(`created_at`) USING BTREE,
  CONSTRAINT `admin_operate_log_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 101 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_operate_log
-- ----------------------------
INSERT INTO `admin_operate_log` VALUES (3, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加标签：测试', '2021-05-15 15:53:57', 1);
INSERT INTO `admin_operate_log` VALUES (4, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加标签：参数', '2021-05-15 16:07:57', 1);
INSERT INTO `admin_operate_log` VALUES (5, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '修改密码', '2021-05-15 16:07:57', 1);
INSERT INTO `admin_operate_log` VALUES (6, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加标签：55', '2021-05-15 17:08:12', 1);
INSERT INTO `admin_operate_log` VALUES (7, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加标签：11', '2021-05-15 17:08:12', 1);
INSERT INTO `admin_operate_log` VALUES (8, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加标签：44', '2021-05-15 17:08:12', 1);
INSERT INTO `admin_operate_log` VALUES (9, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加标签：xxx', '2021-05-15 17:29:53', 1);
INSERT INTO `admin_operate_log` VALUES (10, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加权限：添加标签', '2021-05-15 22:40:46', 1);
INSERT INTO `admin_operate_log` VALUES (11, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除权限添加标签', '2021-05-15 22:51:56', 1);
INSERT INTO `admin_operate_log` VALUES (12, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加权限：添加标签', '2021-05-15 22:51:56', 1);
INSERT INTO `admin_operate_log` VALUES (13, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加权限：编辑标签', '2021-05-15 22:51:56', 1);
INSERT INTO `admin_operate_log` VALUES (14, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加权限：标签列表', '2021-05-15 22:51:56', 1);
INSERT INTO `admin_operate_log` VALUES (15, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加权限：删除标签', '2021-05-15 22:51:56', 1);
INSERT INTO `admin_operate_log` VALUES (16, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加权限：添加电影', '2021-05-15 22:51:56', 1);
INSERT INTO `admin_operate_log` VALUES (17, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加权限：重试', '2021-05-15 23:18:39', 1);
INSERT INTO `admin_operate_log` VALUES (18, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '编辑权限：重试', '2021-05-15 23:19:40', 1);
INSERT INTO `admin_operate_log` VALUES (19, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '编辑权限：重试', '2021-05-15 23:19:40', 1);
INSERT INTO `admin_operate_log` VALUES (20, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '编辑权限：重试11', '2021-05-15 23:24:03', 1);
INSERT INTO `admin_operate_log` VALUES (21, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '编辑权限：重试11', '2021-05-15 23:24:03', 1);
INSERT INTO `admin_operate_log` VALUES (22, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '编辑权限：重试11', '2021-05-15 23:24:03', 1);
INSERT INTO `admin_operate_log` VALUES (23, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除权限重试11', '2021-05-15 23:24:03', 1);
INSERT INTO `admin_operate_log` VALUES (24, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加角色：cs', '2021-05-16 13:14:18', 1);
INSERT INTO `admin_operate_log` VALUES (25, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加角色：css', '2021-05-16 13:15:36', 1);
INSERT INTO `admin_operate_log` VALUES (26, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加角色：cs', '2021-05-16 13:23:37', 1);
INSERT INTO `admin_operate_log` VALUES (27, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加角色：ww', '2021-05-16 13:24:59', 1);
INSERT INTO `admin_operate_log` VALUES (28, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加角色：scsa', '2021-05-16 13:28:03', 1);
INSERT INTO `admin_operate_log` VALUES (29, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除角色：scsa', '2021-05-16 13:44:04', 1);
INSERT INTO `admin_operate_log` VALUES (30, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除角色：ww', '2021-05-16 13:45:30', 1);
INSERT INTO `admin_operate_log` VALUES (33, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '编辑角色：cs', '2021-05-16 14:09:39', 1);
INSERT INTO `admin_operate_log` VALUES (34, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加管理员：admin888', '2021-05-16 16:33:22', 1);
INSERT INTO `admin_operate_log` VALUES (35, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加管理员：1111', '2021-05-16 16:48:51', 1);
INSERT INTO `admin_operate_log` VALUES (36, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加管理员：11111', '2021-05-16 16:48:51', 1);
INSERT INTO `admin_operate_log` VALUES (37, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除管理员：11111', '2021-05-16 16:59:12', 1);
INSERT INTO `admin_operate_log` VALUES (38, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除管理员：1111', '2021-05-16 16:59:12', 1);
INSERT INTO `admin_operate_log` VALUES (39, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加角色：标签管理-1', '2021-05-16 17:43:57', 1);
INSERT INTO `admin_operate_log` VALUES (40, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加管理员：ad', '2021-05-16 17:43:57', 1);
INSERT INTO `admin_operate_log` VALUES (41, 'ad', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加标签：000', '2021-05-16 18:36:54', NULL);
INSERT INTO `admin_operate_log` VALUES (42, 'ad', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '修改标签为：0007', '2021-05-16 18:36:54', NULL);
INSERT INTO `admin_operate_log` VALUES (43, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除角色：cs', '2021-05-18 10:11:24', 1);
INSERT INTO `admin_operate_log` VALUES (44, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除角色：cs', '2021-05-18 10:11:24', 1);
INSERT INTO `admin_operate_log` VALUES (45, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除角色：css', '2021-05-18 10:11:24', 1);
INSERT INTO `admin_operate_log` VALUES (46, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加电影预告：111', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (47, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加电影预告：1213', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (48, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加电影预告：12323', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (49, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加电影预告：scac', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (50, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除电影预告：111', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (51, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除电影预告：1213', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (52, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除电影预告：12323', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (53, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除电影预告：scac', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (54, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '删除电影预告：111', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (55, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加电影预告：周杰伦粉丝版MV', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (56, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加电影预告：乐侃有声节目第二期', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (57, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加电影预告：乐见大牌：”荣“耀之声，”维“我独尊', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (58, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加电影预告：王力宏四年心血结晶', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (59, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '添加电影预告：MV精选：《武媚》女神团美艳大比拼', '2021-05-18 19:36:01', 1);
INSERT INTO `admin_operate_log` VALUES (60, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影：cs', '2021-05-19 11:30:01', 1);
INSERT INTO `admin_operate_log` VALUES (61, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除管理员：ad', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (62, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除管理员：admin888', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (63, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除角色：标签管理-1', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (64, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除电影预告：周杰伦粉丝版MV', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (65, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除电影预告：乐侃有声节目第二期', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (66, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除电影预告：乐见大牌：”荣“耀之声，”维“我独尊', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (67, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除电影预告：王力宏四年心血结晶', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (68, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除电影预告：王力宏四年心血结晶', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (69, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除电影预告：MV精选：《武媚》女神团美艳大比拼', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (70, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影预告：哆啦A梦：伴我同行2  STAND BY ME ドラえもん2', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (71, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '编辑电影预告：哆啦A梦：伴我同行2  STAND BY ME ドラえもん2', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (72, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影预告：九零后', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (73, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影预告：深爱 Deep Love', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (74, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影预告：2哥来了怎么办', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (75, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影预告：我没谈完的那场恋爱', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (76, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影预告：再见，少年', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (77, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影预告：古董局中局', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (78, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影预告：匹诺曹', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (79, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '添加电影预告：有一点动心', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (80, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：cs', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (81, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：111', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (82, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：100', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (83, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：哆啦A梦：伴我同行2  STAND BY ME ドラえもん2', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (84, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：深爱 Deep Love', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (85, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：再见，少年', '2021-05-21 10:54:44', 1);
INSERT INTO `admin_operate_log` VALUES (86, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：哆啦A梦：伴我同行2  STAND BY ME ドラえもん2', '2021-05-21 12:05:11', 1);
INSERT INTO `admin_operate_log` VALUES (87, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：深爱 Deep Love', '2021-05-21 12:05:11', 1);
INSERT INTO `admin_operate_log` VALUES (88, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：再见，少年', '2021-05-21 12:05:11', 1);
INSERT INTO `admin_operate_log` VALUES (89, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：哆啦A梦：伴我同行2  STAND BY ME ドラえもん2', '2021-05-21 12:05:11', 1);
INSERT INTO `admin_operate_log` VALUES (90, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：深爱 Deep Love', '2021-05-21 12:05:11', 1);
INSERT INTO `admin_operate_log` VALUES (91, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '修改电影：再见，少年', '2021-05-21 12:05:11', 1);
INSERT INTO `admin_operate_log` VALUES (92, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除标签', '2021-05-21 15:47:40', 1);
INSERT INTO `admin_operate_log` VALUES (93, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除标签', '2021-05-21 15:47:40', 1);
INSERT INTO `admin_operate_log` VALUES (94, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除标签', '2021-05-21 15:47:40', 1);
INSERT INTO `admin_operate_log` VALUES (95, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除标签', '2021-05-21 15:47:40', 1);
INSERT INTO `admin_operate_log` VALUES (96, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除标签', '2021-05-21 15:47:40', 1);
INSERT INTO `admin_operate_log` VALUES (97, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除标签', '2021-05-21 15:47:40', 1);
INSERT INTO `admin_operate_log` VALUES (98, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除标签', '2021-05-21 15:47:40', 1);
INSERT INTO `admin_operate_log` VALUES (99, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除标签', '2021-05-21 15:47:40', 1);
INSERT INTO `admin_operate_log` VALUES (100, 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '删除标签', '2021-05-21 15:47:40', 1);

-- ----------------------------
-- Table structure for auth
-- ----------------------------
DROP TABLE IF EXISTS `auth`;
CREATE TABLE `auth`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限id',
  `name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '权限名称',
  `url` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '权限路径',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ix_auth_created_at`(`created_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 38 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth
-- ----------------------------
INSERT INTO `auth` VALUES (2, '添加标签', '/tag_add/', '2021-05-15 22:51:56');
INSERT INTO `auth` VALUES (3, '编辑标签', '/tag_edit/<int:tag_id>/', '2021-05-15 22:51:56');
INSERT INTO `auth` VALUES (4, '标签列表', '/tag_list/<int:page>/', '2021-05-15 22:51:56');
INSERT INTO `auth` VALUES (5, '删除标签', '/tag_del/<int:tag_id>/', '2021-05-15 22:51:56');
INSERT INTO `auth` VALUES (6, '添加电影', '/movie_add/', '2021-05-15 22:51:56');
INSERT INTO `auth` VALUES (7, '编辑电影', '/movie_edit/<int:movie_id>/', '2021-05-15 22:59:13');
INSERT INTO `auth` VALUES (8, '电影列表', '/movie_list/<int:page>/', '2021-05-15 22:59:19');
INSERT INTO `auth` VALUES (9, '删除电影', '/movie_del/<int:movie_id>/', '2021-05-15 22:59:59');
INSERT INTO `auth` VALUES (10, '添加预告', '/preview_add/', '2021-05-15 23:00:17');
INSERT INTO `auth` VALUES (11, '预告列表', '/preview_list/<int:page>/', '2021-05-15 23:00:21');
INSERT INTO `auth` VALUES (12, '删除预告', '/preview_del/<int:prev_id>/', '2021-05-15 23:00:43');
INSERT INTO `auth` VALUES (13, '编辑预告', '/preview_edit/<int:prev_id>/', '2021-05-15 23:01:14');
INSERT INTO `auth` VALUES (14, '用户详情', '/user_view/<int:user_id>/', '2021-05-15 23:01:47');
INSERT INTO `auth` VALUES (15, '用户列表', '/user_list/<int:page>/', '2021-05-15 23:02:04');
INSERT INTO `auth` VALUES (16, '删除用户', '/user_del/<int:user_id>/', '2021-05-15 23:02:16');
INSERT INTO `auth` VALUES (17, '禁用用户', '/user_disable/<int:user_id>/', '2021-05-15 23:02:33');
INSERT INTO `auth` VALUES (18, '启用用户', '/user_enable/<int:user_id>/', '2021-05-15 23:02:55');
INSERT INTO `auth` VALUES (19, '评论列表', '/comment_list/<int:page>/', '2021-05-15 23:03:05');
INSERT INTO `auth` VALUES (20, '删除评论', '/comment_del/<int:comment_id>/', '2021-05-15 23:03:18');
INSERT INTO `auth` VALUES (21, '电影收藏列表', '/movie_collect_list/<int:page>/', '2021-05-15 23:03:38');
INSERT INTO `auth` VALUES (22, '删除收藏电影', '/movie_collect_del/<int:collect_id>/', '2021-05-15 23:03:53');
INSERT INTO `auth` VALUES (23, '管理员操作日志', '/admin_operate_log_list/<int:page>/', '2021-05-15 23:04:07');
INSERT INTO `auth` VALUES (24, '管理员登录日志', '/admin_login_log_list/<int:page>/', '2021-05-15 23:04:17');
INSERT INTO `auth` VALUES (25, '用户登录日志', '/user_login_log_list/<int:page>/', '2021-05-15 23:04:29');
INSERT INTO `auth` VALUES (27, '添加权限', '/auth_add/', '2021-05-18 10:08:33');
INSERT INTO `auth` VALUES (28, '编辑权限', '/auth_edit/<int:auth_id>/', '2021-05-18 10:08:52');
INSERT INTO `auth` VALUES (29, '删除权限', '/auth_del/<int:auth_id>/', '2021-05-18 10:09:07');
INSERT INTO `auth` VALUES (30, '权限列表', '/auth_list/<int:page>/', '2021-05-18 10:09:27');
INSERT INTO `auth` VALUES (31, '添加角色', '/role_add/', '2021-05-18 10:09:42');
INSERT INTO `auth` VALUES (32, '角色列表', '/role_list/<int:page>/', '2021-05-18 10:10:00');
INSERT INTO `auth` VALUES (33, '删除角色', '/role_del/<int:role_id>/', '2021-05-18 10:10:10');
INSERT INTO `auth` VALUES (34, '编辑角色', '/role_edit/<int:role_id>/', '2021-05-18 10:10:23');
INSERT INTO `auth` VALUES (35, '添加管理员', '/admin_add/', '2021-05-18 10:10:40');
INSERT INTO `auth` VALUES (36, '管理员列表', '/admin_list/<int:page>/', '2021-05-18 10:10:55');
INSERT INTO `auth` VALUES (37, '删除管理员', '/admin_del/<int:admin_id>/', '2021-05-18 10:11:26');

-- ----------------------------
-- Table structure for movie
-- ----------------------------
DROP TABLE IF EXISTS `movie`;
CREATE TABLE `movie`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '电影id',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '电影名称',
  `url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '电影链接',
  `info` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '电影简介',
  `logo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '电影封面',
  `area` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '上映地区',
  `release_date` date NULL DEFAULT NULL COMMENT '上映日期',
  `movie_length` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '电影时长',
  `star` smallint(6) NULL DEFAULT NULL COMMENT '星级',
  `play_count` bigint(20) NULL DEFAULT NULL COMMENT '播放统计',
  `comment_count` bigint(20) NULL DEFAULT NULL COMMENT '评论统计',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '添加时间',
  `tag_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tag_id`(`tag_id`) USING BTREE,
  INDEX `ix_movie_created_at`(`created_at`) USING BTREE,
  CONSTRAINT `movie_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `movie_tag` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of movie
-- ----------------------------
INSERT INTO `movie` VALUES (3, '再见，少年', '20210514111342d9dcdcf6470e47bca9352bd01de9cdd2.mp4', '影片讲述了千禧年发生在南方小镇上的一段曾经无限接近，却又渐行渐远的少年情谊。“好学生”黎菲与“坏孩子”张辰浩，各自经历了时代大潮下家庭的变迁，一起奋力而坚韧地成长。然而高考前的一场剧变，让青春笼上阴影，最终裹挟住了二人的命运。', '202105211152024f28e5c4e270462a8fe2b9cf612571e1.jpg', '大陆', '2021-05-22', '30', 3, 77, 8, '2021-05-13 22:41:40', 2);
INSERT INTO `movie` VALUES (4, '深爱 Deep Love', '2021051322482053f6a243913841248cf58b29532f89b0.mp4', '“在这座城市里拥有爱情，我配么？”这也许是每一个“漂一族”的自我怀疑。一次交通意外，让王惜月（王智饰）陷入了一场从未预想的“一见钟情”；同为职场精英的何娜（克拉拉饰），一贯洒脱对待爱情的心态也面临着动摇。这个原本对她们来说只是生存战场的城市，突然变得更为复杂了……谎言之上的爱情岌岌可危，朋友名义下的快乐转瞬即逝，两段需要抉择的“深爱”，她们的答案，是否会和你一样？', '20210521115149d571a22d85944cb69edf052bc0e5ee5c.jpg', '大陆', '2021-05-26', '1', 1, 11, 0, '2021-05-13 22:47:53', 2);
INSERT INTO `movie` VALUES (5, '哆啦A梦：伴我同行2  STAND BY ME ドラえもん2', '202105191131443fff304a6639414c98253eec21185c04.mp4', '时隔6年，动画电影“伴我同行”系列回归，同时本片也是该系列的终章。大雄为了实现奶奶看到妻子的愿望，想坐着时光机去未来参加他的婚礼，但爱情长跑50年终于要娶到静香的大雄竟然想逃婚…', '20210521115142352f8d2c0c174bb59e8dd018486615eb.jpg', '大陆', '2021-05-29', '5', 4, 25, 2, '2021-05-19 11:30:01', 10);

-- ----------------------------
-- Table structure for movie_collect
-- ----------------------------
DROP TABLE IF EXISTS `movie_collect`;
CREATE TABLE `movie_collect`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '电影收藏id',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '收藏时间',
  `movie_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `movie_id`(`movie_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `ix_movie_collect_created_at`(`created_at`) USING BTREE,
  CONSTRAINT `movie_collect_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `movie_collect_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of movie_collect
-- ----------------------------
INSERT INTO `movie_collect` VALUES (8, '2021-05-20 18:33:43', 3, 5);
INSERT INTO `movie_collect` VALUES (9, '2021-05-20 19:20:08', 4, 5);

-- ----------------------------
-- Table structure for movie_comment
-- ----------------------------
DROP TABLE IF EXISTS `movie_comment`;
CREATE TABLE `movie_comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '评论id',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '评论内容',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '添加时间',
  `movie_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `movie_id`(`movie_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `ix_movie_comment_created_at`(`created_at`) USING BTREE,
  CONSTRAINT `movie_comment_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `movie_comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of movie_comment
-- ----------------------------
INSERT INTO `movie_comment` VALUES (2, '<p><img src=\"http://img.baidu.com/hi/jx2/j_0001.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0045.gif\"/>cs</p>', '2021-05-19 15:18:17', 3, 5);
INSERT INTO `movie_comment` VALUES (3, '<p><img src=\"http://img.baidu.com/hi/jx2/j_0013.gif\"/></p>', '2021-05-19 15:18:17', 3, 5);
INSERT INTO `movie_comment` VALUES (4, '<p><img src=\"http://img.baidu.com/hi/jx2/j_0065.gif\"/></p>', '2021-05-19 15:18:17', 3, 5);
INSERT INTO `movie_comment` VALUES (5, '<p><img src=\"http://img.baidu.com/hi/jx2/j_0005.gif\"/></p>', '2021-05-19 15:18:17', 3, 5);
INSERT INTO `movie_comment` VALUES (6, '<p><img src=\"http://img.baidu.com/hi/jx2/j_0032.gif\"/></p>', '2021-05-19 15:18:17', 3, 5);
INSERT INTO `movie_comment` VALUES (7, '<p><img src=\"http://img.baidu.com/hi/jx2/j_0064.gif\"/></p>', '2021-05-19 15:18:17', 3, 5);
INSERT INTO `movie_comment` VALUES (8, '<p><img src=\"http://img.baidu.com/hi/jx2/j_0033.gif\"/></p>', '2021-05-19 15:18:17', 3, 5);
INSERT INTO `movie_comment` VALUES (9, '<p><img style=\"background-position:left -1121px;\" title=\"扯花\" src=\"http://img.baidu.com/hi/default/0.gif\" width=\"35\" height=\"35\"/>a</p>', '2021-05-19 15:18:17', 3, 5);
INSERT INTO `movie_comment` VALUES (10, '<p><img src=\"http://img.baidu.com/hi/jx2/j_0015.gif\"/></p>', '2021-05-20 10:49:36', 5, 5);
INSERT INTO `movie_comment` VALUES (11, '<p>11<br/></p>', '2021-05-20 10:49:36', 5, 5);

-- ----------------------------
-- Table structure for movie_preview
-- ----------------------------
DROP TABLE IF EXISTS `movie_preview`;
CREATE TABLE `movie_preview`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '电影上映预告id',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '电影上映预告名称',
  `info` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '电影上映预告简介',
  `logo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '电影上映预告封面',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '添加时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ix_movie_preview_created_at`(`created_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of movie_preview
-- ----------------------------
INSERT INTO `movie_preview` VALUES (12, '哆啦A梦：伴我同行2  STAND BY ME ドラえもん2', '时隔6年，动画电影“伴我同行”系列回归，同时本片也是该系列的终章。大雄为了实现奶奶看到妻子的愿望，想坐着时光机去未来参加他的婚礼，但爱情长跑50年终于要娶到静香的大雄竟然想逃婚…', '202105211101543bd65b23068b4e89a4dc8554e3d15361.jpg', '2021-05-21 10:54:44');
INSERT INTO `movie_preview` VALUES (13, '九零后', '故土在战争中沦陷，大学被占领、被炸毁。一群十八九岁的青年学生，他们匆匆出发，徒步南迁，穿越湘黔滇三省，最终在昆明组建临时大学——由清华、北大、南开联合成立的西南联大。他们穿过一座城去听“史上最好的国文课”，听托赛里的《小夜曲》，也和先生们一起抱着书跑警报、加入飞虎队……对这些今已年过九旬的“九零后”老人而言，西南联大不是尘封的历史，而是鲜活如初的青春记忆。杨振宁、许渊冲、杨苡、潘际銮、王希季、马识途……16位平均年龄超过96岁的联大学子联袂“出演”，带你去往那个战火纷飞、群星闪耀的年代。', '202105211115162c1e9639eb814243b155be06be3e46e2.jpg', '2021-05-21 10:54:44');
INSERT INTO `movie_preview` VALUES (14, '深爱 Deep Love', '“在这座城市里拥有爱情，我配么？”这也许是每一个“漂一族”的自我怀疑。一次交通意外，让王惜月（王智饰）陷入了一场从未预想的“一见钟情”；同为职场精英的何娜（克拉拉饰），一贯洒脱对待爱情的心态也面临着动摇。这个原本对她们来说只是生存战场的城市，突然变得更为复杂了……谎言之上的爱情岌岌可危，朋友名义下的快乐转瞬即逝，两段需要抉择的“深爱”，她们的答案，是否会和你一样？', '2021052111181468a5e1ef6c0241569348d776965d1a25.jpg', '2021-05-21 10:54:44');
INSERT INTO `movie_preview` VALUES (15, '2哥来了怎么办', '故事讲述了关于重组家庭里吵闹而又温馨的那些事。杨听风杨听雨是一对兄妹，自从杨妈妈与李叔叔再婚后，五花八门的尴尬大戏便在重组家庭中一直上演。这一天，不速之客李圣突然出现，平静的生活就此乱套……天降2哥？父母偏心？亲哥也倒戈？这一连串的巨变令杨听雨不堪忍受，只想大喊一句：2哥来了怎么办！', '20210521114142967e306a72bf40f1a9a95fac4a618fc9.jpg', '2021-05-21 10:54:44');
INSERT INTO `movie_preview` VALUES (16, '我没谈完的那场恋爱', '本片讲述了两个千差万别却同样迷茫的年轻音乐人，一个是多年打拼,事业毫无起色,又屡遭生活暴击的和声歌手珊妮,一个是身患重病,隐姓埋名等待死亡降临的前摇滚乐手董东,对生命感到绝望的二人在自我了断时相遇......自杀计划流产,他们的生活也因彼此的出现发生改变。另外一个时空的故事,从珊妮意外发现的一本1970年代的日记中铺陈开来,一段没有下文的悲伤爱情竟然在珊妮的努力下尘埃落定。跟音乐、爱情和人生有关的种种,让珊妮与董东的相遇愈发神奇。千丝万缕中,是否每一种爱都能开花结果? 他们能否找到继续爱这个世界的理由?', '20210521114247b1875a2ce0c940909083bfa4d43f6452.jpg', '2021-05-21 10:54:44');
INSERT INTO `movie_preview` VALUES (17, '再见，少年', '影片讲述了千禧年发生在南方小镇上的一段曾经无限接近，却又渐行渐远的少年情谊。“好学生”黎菲与“坏孩子”张辰浩，各自经历了时代大潮下家庭的变迁，一起奋力而坚韧地成长。然而高考前的一场剧变，让青春笼上阴影，最终裹挟住了二人的命运。', '202105211143523eb5f59c585146f5bb23c1c90eccbf9a.jpg', '2021-05-21 10:54:44');
INSERT INTO `movie_preview` VALUES (18, '古董局中局', '来自日本的木户小姐（松峰莉璃 饰）即将向中国归还一尊唐代武则天明堂佛头，却指明要文物界权威组织“五脉”旗下白字门许家后人出面接收。但五脉白字门早已没落，许家后人也不知所踪。情势紧张，五脉掌门黄克武的孙女黄烟烟（辛芷蕾 饰）却表示，自己有办法找到许家后人的踪迹。而当初背负汉奸骂名，将佛头送去日本的白字门家主许一城之孙——许愿（雷佳音 饰），有一身鉴古天赋的他，如今只是一个胸无大志的电器铺小老板，靠倒卖电器勉强维持生计。许愿幼年时因为一场火灾失去了母亲，而父亲许和平在火灾之后便对他保持着疏离的态度，不仅如此，他还要承受着外界对自己家族的骂名——时至今日，在黄烟烟的劝说下，他不情愿的前往与五脉交涉，却敏锐地察觉到佛头是赝品的事实。常年以来浑浑噩噩的生活让许愿习惯性地选择逃避——然而面对着黄烟烟的委托、父亲许和平的离奇死亡、五脉天才药不然（李现 饰）的逼迫、祖父故交付贵（葛优 饰）的追随与神秘人老朝奉（秦焰 饰）的追击之下，许愿已经身不由己。他必须要在各方势力的纠缠之下，查明佛头真相……', '202105211144482f96ee7dfdab436889db525f519d1b60.jpg', '2021-05-21 10:54:44');
INSERT INTO `movie_preview` VALUES (19, '匹诺曹', '意大利真人版《匹诺曹》，故事围绕一个老木匠与他雕刻的小木偶匹诺曹展开。', '20210521114528ecd56b03966f4b20999d19337f1909dc.jpg', '2021-05-21 10:54:44');
INSERT INTO `movie_preview` VALUES (20, '有一点动心', '周启文（言承旭 饰）创立的游戏公司因旗下员工直播的“渣男”言论引起全网声讨，被迫宣告破产，他带着兄弟们去找“始作俑者”相亲APP员工讨个说法。虽然打着成为对方客户，搅黄她们生意的坏主意，但周启文却被对方女老板陈然（任素汐 饰）安排得明明白白。在不断的相亲过程中，二人逐渐卸下了对彼此的敌意和伪装，互相的了解让二人间萌生情愫。在这越来越不敢爱的时代，周启文和陈然是会就此错过，还是能抓住命运不顾一切付出真心？', '2021052111455353a7b375c169465aae4178826a178650.jpg', '2021-05-21 10:54:44');

-- ----------------------------
-- Table structure for movie_tag
-- ----------------------------
DROP TABLE IF EXISTS `movie_tag`;
CREATE TABLE `movie_tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '标签id',
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '标签名',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ix_movie_tag_created_at`(`created_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of movie_tag
-- ----------------------------
INSERT INTO `movie_tag` VALUES (1, '科幻', '2021-05-12 11:55:06');
INSERT INTO `movie_tag` VALUES (2, '爱情', '2021-05-12 15:45:07');
INSERT INTO `movie_tag` VALUES (3, '动作', '2021-05-12 15:45:07');
INSERT INTO `movie_tag` VALUES (4, '古装', '2021-05-12 15:45:07');
INSERT INTO `movie_tag` VALUES (5, '武侠', '2021-05-12 15:45:07');
INSERT INTO `movie_tag` VALUES (6, '恐怖', '2021-05-12 15:45:07');
INSERT INTO `movie_tag` VALUES (7, '惊悚', '2021-05-12 15:45:07');
INSERT INTO `movie_tag` VALUES (8, '犯罪', '2021-05-12 15:45:07');
INSERT INTO `movie_tag` VALUES (9, '喜剧', '2021-05-12 15:45:07');
INSERT INTO `movie_tag` VALUES (10, '动画', '2021-05-12 15:45:07');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色id',
  `name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色名称',
  `auths` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '角色权限列表',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ix_role_created_at`(`created_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (1, '超级管理员', '2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37', '2021-05-13 22:22:54');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户账号',
  `password` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `nickname` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '昵称',
  `email` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '邮箱',
  `phone` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `info` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '用户简介',
  `status` enum('USER_ACTIVE','USER_IN_ACTIVE') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户状态',
  `avatar` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '头像',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `updated_at` datetime(0) NULL DEFAULT NULL COMMENT '最后登录时间',
  `uuid` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '唯一标识符',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ix_user_created_at`(`created_at`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (2, '111111', 'pbkdf2:sha256:150000$K2imHYvh$2f9b17b41aea8d620326da05c79d526e81f7ed96093e09282524868846c1a7e9', '111111', '11@11.com', '11111111111', '111', 'USER_ACTIVE', '5255', '2021-05-15 09:10:44', '2021-05-15 09:10:46', '11111111111');
INSERT INTO `user` VALUES (3, '11111122', 'pbkdf2:sha256:150000$K2imHYvh$2f9b17b41aea8d620326da05c79d526e81f7ed96093e09282524868846c1a7e9', '', '111@1.ccc', '15111111111', NULL, 'USER_ACTIVE', NULL, '2021-05-17 17:19:29', '2021-05-17 17:19:29', 'c7463f6eb9be4a62a26b39a18d3db6b5');
INSERT INTO `user` VALUES (4, '2222222', 'pbkdf2:sha256:150000$UbtywgkJ$2c23ed4486aa4484e0947abd4ced141962f5f46b273c3e9b3a1fed6e372fdaec', '', '11@dd.bb', '13133114111', NULL, 'USER_ACTIVE', NULL, '2021-05-17 21:43:14', '2021-05-17 21:43:14', '35baf5aee5294f45baff7c1acc671997');
INSERT INTO `user` VALUES (5, '1112223', 'pbkdf2:sha256:150000$yYVcqQtb$7f25cdbdc94ceb4445beb233bf039a14e194a7471d797ff52aae29cd6eabc05a', '', '123@qq.com', '13432234652', '', 'USER_ACTIVE', '202105181708587ab62064a9ec4f69bd3d7eafd8d21a9a.jpg', '2021-05-17 22:34:41', '2021-05-18 18:51:50', '1fcd0e857da74f089d808cfe34d546cd');

-- ----------------------------
-- Table structure for user_log
-- ----------------------------
DROP TABLE IF EXISTS `user_log`;
CREATE TABLE `user_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '日志id',
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '会员用户名',
  `ip` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '登录ip',
  `login_type` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '账号平台',
  `ua` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'user-agent',
  `created_at` datetime(0) NULL DEFAULT NULL COMMENT '登录时间',
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `ix_user_log_created_at`(`created_at`) USING BTREE,
  CONSTRAINT `user_log_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_log
-- ----------------------------
INSERT INTO `user_log` VALUES (1, '111111', '111', '11', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-15 18:05:02', 2);
INSERT INTO `user_log` VALUES (2, '1112223', '127.0.0.1', 'PC', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-17 22:39:04', 5);
INSERT INTO `user_log` VALUES (3, '1112223', '127.0.0.1', 'PC', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-17 22:39:04', 5);
INSERT INTO `user_log` VALUES (4, '1112223', '127.0.0.1', 'PC', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-17 22:40:31', 5);
INSERT INTO `user_log` VALUES (5, '1112223', '127.0.0.1', 'PC', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-17 22:48:15', 5);
INSERT INTO `user_log` VALUES (6, '1112223', '127.0.0.1', 'PC', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-17 22:48:15', 5);
INSERT INTO `user_log` VALUES (7, '1112223', '127.0.0.1', 'PC', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-18 10:30:09', 5);
INSERT INTO `user_log` VALUES (8, '1112223', '127.0.0.1', 'PC', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', '2021-05-18 18:51:50', 5);
INSERT INTO `user_log` VALUES (9, '1112223', '127.0.0.1', 'PC', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '2021-05-19 11:47:08', 5);
INSERT INTO `user_log` VALUES (10, '1112223', '127.0.0.1', 'PC', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', '2021-05-19 11:47:08', 5);

SET FOREIGN_KEY_CHECKS = 1;
