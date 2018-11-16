#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import step, given, when, then

@when('зайти на сайт {url}')
def open_url(context, url):
    context.browser.get(url)
    
@when('нажать на ссылку "{link_text}"')
def link_click(context, link_text):
    link = context.browser.find_element_by_xpath('//div[@class="lang-switch"]/a')
    assert link, 'ссылка ' + link_text + ' не найдена'
    link.click()
    
@then('url страницы станет {url}')
def assert_url(context, url):
    current_url = context.browser.current_url
    assert current_url == url, 'url страницы не соответствует ожидаемому'    
    
@then('на странице будет текст "{text}"')
def find_text(context, text):
    page = context.browser.find_element_by_xpath('//div[@class="slogan"]')
    page_text = page.text
    assert text in page_text[:len(text)], 'на странице не найден текст: ' + text
